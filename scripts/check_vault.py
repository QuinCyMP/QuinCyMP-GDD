#!/usr/bin/env python3
"""Report broken wikilinks and inconsistent open-question counts in a vault."""

import argparse
import bisect
import posixpath
import re
from pathlib import Path


INLINE_CODE = r"(?<![\\`])(?P<ticks>`+)(?!`)(?P<code_text>.*?)(?<!`)(?P=ticks)(?!`)"
CODE_SPAN = re.compile(INLINE_CODE, re.DOTALL)
# Consume each complete construct before looking inside it. For example, a
# fence inside an HTML comment must not hide prose after that comment ends.
LITERAL = re.compile(
    r"(?P<backtick_block>^ {0,3}(?P<backticks>`{3,})(?!`)[^`\n]*(?:\n|$).*?"
    r"(?:^ {0,3}(?P=backticks)`*[ \t]*(?:\n|$)|\Z))"
    r"|(?P<tilde_block>^ {0,3}(?P<tildes>~{3,})(?!~)[^\n]*(?:\n|$).*?"
    r"(?:^ {0,3}(?P=tildes)~*[ \t]*(?:\n|$)|\Z))"
    r"|(?P<indented>^(?: {4}|\t)[^\n]*(?:\n|$))"
    r"|(?P<comment><!--.*?(?:-->|\Z))"
    r"|(?P<inline>" + INLINE_CODE + r")",
    re.MULTILINE | re.DOTALL,
)
WIKILINK = re.compile(r"(?<!\\)\[\[([^\]\n]*)\]\]")


def blank(text):
    """Hide syntax without changing the offsets used for line numbers."""
    return re.sub(r"[^\n]", " ", text)


def markdown_body(text):
    """Mask front matter, fenced/indented code and HTML comments."""
    lines = text.splitlines(keepends=True)
    front_matter = bool(lines and lines[0].strip() == "---")
    for index, line in enumerate(lines):
        if front_matter:
            lines[index] = blank(line)
            if index and line.strip() == "---":
                break
        else:
            break
    return LITERAL.sub(lambda m: m[0] if m["inline"] else blank(m[0]), "".join(lines))


def heading_text(text):
    text = CODE_SPAN.sub(lambda m: m["code_text"], text)
    return re.sub(r"(?<!\w)(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1(?!\w)", r"\2", text).strip()


def headings(body):
    result = set()
    previous = ""
    for line in body.splitlines():
        atx = re.match(r" {0,3}#{1,6}(?:[ \t]+|$)(.*)", line)
        if atx:
            title = re.sub(r"[ \t]+#+[ \t]*$", "", atx[1]).strip()
            result.add(heading_text(title))
        elif previous.strip() and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", line):
            result.add(heading_text(previous))
        previous = line
    return result


def marker_problems(text):
    """Check a top-level integer field, without needing a YAML dependency."""
    lines = text.splitlines()
    count = text.count("[UNDECIDED")
    fields = []
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], 2):
            if line.strip() == "---":
                break
            match = re.match(r"^open-questions:\s*(.*?)\s*$", line)
            if match:
                fields.append((index, match[1]))
        else:
            return [(1, "unclosed front matter")]
    if not fields:
        return [(1, "missing open-questions field for %d markers" % count)] if count else []
    if len(fields) > 1:
        return [(line, "duplicate open-questions field") for line, value in fields[1:]]
    line, value = fields[0]
    match = re.fullmatch(r"([0-9]+)(?:\s+#.*)?", value)
    if not match:
        return [(line, "open-questions must be a non-negative integer")]
    if int(match[1]) != count:
        return [(line, "open-questions is %s but found %d [UNDECIDED markers" % (match[1], count))]
    return []


def resolve_file(source, name, files):
    """Resolve explicit paths, nearby notes, then unique basenames in the vault."""
    if name.startswith(("./", "../")):
        locations = [posixpath.join(posixpath.dirname(source), name)]
    elif "/" in name:
        locations = [name.lstrip("/")]
    else:
        locations = [posixpath.join(posixpath.dirname(source), name), name]
    for location in locations:
        location = posixpath.normpath(location)
        if location == ".." or location.startswith("../"):
            return None, "link points outside the vault"
        candidates = [location] if location.endswith(".md") else [location, location + ".md"]
        for candidate in candidates:
            if candidate in files:
                return candidate, None
    if "/" not in name:
        names = {name} if name.endswith(".md") else {name, name + ".md"}
        matches = sorted(path for path in files if posixpath.basename(path) in names)
        if len(matches) == 1:
            return matches[0], None
        if len(matches) > 1:
            return None, "ambiguous file %r; use a folder path" % name
    return None, "missing file %r" % name


def check_vault(root):
    files = {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*") if not path.is_symlink() and path.is_file()
    }
    documents = {}
    problems = []
    for name, path in sorted(files.items()):
        if path.suffix.lower() != ".md":
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            problems.append((name, 1, "cannot read Markdown: %s" % error))
            continue
        problems.extend((name, line, message) for line, message in marker_problems(text))
        body = markdown_body(text)
        documents[name] = (body, headings(body))

    for name, (body, titles) in sorted(documents.items()):
        visible = CODE_SPAN.sub(lambda m: blank(m[0]), body)
        newlines = [index for index, char in enumerate(visible) if char == "\n"]
        for match in WIKILINK.finditer(visible):
            line = bisect.bisect_right(newlines, match.start()) + 1
            # A table escapes the alias separator as \|, but it is still an alias.
            target = match[1].replace(r"\|", "|").split("|", 1)[0].strip()
            filename, separator, heading = target.partition("#")
            if filename:
                destination, error = resolve_file(name, filename, files)
                if error:
                    problems.append((name, line, error))
                    continue
            elif separator:
                destination = name
            else:
                problems.append((name, line, "empty wikilink"))
                continue
            if separator:
                if heading.startswith("^") or "#" in heading:
                    problems.append((name, line, "unsupported heading reference %r; use one heading title" % heading))
                elif destination not in documents:
                    problems.append((name, line, "cannot check heading in %r" % destination))
                elif heading.strip() not in documents[destination][1]:
                    problems.append((name, line, "missing heading %r in %r" % (heading, destination)))
    return sorted(problems)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="vault folder to check recursively")
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error("folder must be an existing directory")
    problems = check_vault(args.folder)
    for filename, line, message in problems:
        print("%s:%d: %s" % (filename, line, message))
    if not problems:
        print("No link or marker problems found.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
