# Phase B: the living vault

Read this before touching any file in a project that already has dozens of design documents.

In Phase A the risk is writing beautifully without deciding. In Phase B the risk is deciding again while forgetting the opposite was already decided. A contradictory document is worse than an incomplete one: an incomplete document says what is unknown, a contradictory one leaves the reader unsure which line to believe, so they stop believing all of it.

## 1. Four checks before writing a line

| | Check | How |
|---|---|---|
| 1 | **Does this topic already have a home?** | `grep -ril "<keyword>"`. If a file owns it, write there. Do not open a new home. |
| 2 | **Does the system about to be referenced exist in the vault?** | A skill that cites a system that does not exist is a skill that gets torn out later. |
| 3 | **Which sentence does the new thing make false?** | Search for the direct negation. Adding a class system: search `"no class system"`. |
| 4 | **Does a neighbouring file use the same word?** | Two files both using "formation" or "signal" means the boundary between them has not been drawn. |

## 2. Single home

> Every rule has exactly one home. Everything else links to it.

One rule written in three files is not emphasis three times; it is three versions that disagree in two years, because whoever edits it finds only one.

Find duplicates with the rule's most distinctive sentence:

```bash
grep -rn "the memorable sentence" --include="*.md" .
```

More than one file means a home must be chosen:

| The rule is about | Home |
|---|---|
| A number or its unit | The file that defines the number |
| A rule spanning several systems | The central rules file, not the first file that used it |
| Something one job, class or system uses | That thing's own file |

Never delete a copy outright. Replace it with a one-line link, or readers who remember it there will think the rule is gone.

## 3. Machine-readable markers

An undecided point must be a string a script can find, not a graceful sentence in a paragraph:

```markdown
[UNDECIDED: <the question to answer>]
[PROVISIONAL: <the value>]
```

Front matter must always match the real count:

```yaml
---
open-questions: 6
---
```

From this skill's root, check the whole vault with Python 3.8 or newer:

```bash
python scripts/check_vault.py ./design
```

The [checker](../scripts/check_vault.py) scans Markdown files recursively and prints
each link or marker problem as `file:line: message`.
It exits with code 1 when it finds a problem, 0 when both checks pass, or 2 when the
folder argument is invalid.
It does not change any files.

The count includes every literal `[UNDECIDED` occurrence, including examples in code.
Use one top-level `open-questions:` field with a non-negative integer in the opening
`---` front matter; an inline YAML comment after the number is allowed.
Missing metadata is reported when markers exist.
A file without markers or a count, such as an older scaffold's glossary, passes.

The most common and most dangerous symptom: front matter says `open-questions: 3` and the body has no marker at all. The real open work has vanished from every board and every query. Nobody will see it again.

## 4. Links

In a vault that uses wikilinks (`[[file#heading|text]]`), a broken link raises no error. It goes quiet.

| Layer | Check |
|---|---|
| **File link** | `[[filename]]` points to a file that exists |
| **Heading link** | `[[file#heading]]`: the heading still has that exact name. Breaks most often when headings are edited. |

Run the same checker after editing or renaming files.
It understands `.md` extensions, aliases including escaped `\|` in tables, same-file
heading links, and links to attachments with an explicit extension.
These forms follow [Obsidian's internal-link syntax](https://help.obsidian.md/links).
Links inside inline code, fenced or indented code, front matter and HTML comments
are skipped.

Folder-qualified links start at the vault root.
An explicit `./` or `../` path starts at the source file's folder and must stay in
the vault.
A bare filename first checks that folder, then the vault root, then a unique name
anywhere in the vault.
Ambiguous names need a folder path.
Paths and heading names are case-sensitive.

Heading checks support one ATX (`## Heading`) or Setext heading title, including
inline code and basic emphasis in the title.
Block IDs and chained subheading paths are reported as unsupported references.
Ordinary Markdown links and HTML headings are not checked.
Symbolic links are not followed.
Boundary-word checks remain manual because the example table below does not define
a machine-readable configuration.

## 5. Contradiction hunting

| Symptom | How to find it | Real example |
|---|---|---|
| **Dead text still cited** | Search for retired system names | One file says a system was replaced, but the source still carries the old one and six files cite the source |
| **One number, two values** | Search for the number across the vault | A cap written as `~30%` in one place, `60%` in the file that uses it |
| **One word, two meanings** | Search the word, read each context | `30%` meaning trained skill in one file and total power in another |
| **Two files own one topic** | Look for similar headings | File A and file B both have "Fronts and signals" |
| **New thing makes old text false** | After a large addition, search its negation | 254 classes added while two files still say "there is no class system" |

### What to do with findings

Do not fix it yourself when it is the owner's decision. Write a conflicts file, one entry per conflict:

```markdown
## C4 · <short name>

| Where | Says |
|---|---|
| [[file A]] line 96 | *"exact quote"* |
| [[file B]] line 305 | *"exact quote"* |

| Option | Consequence |
|---|---|
| **A** | ... (recommended) |
| **B** | ... |
```

Quote the exact text, never a summary. The owner must see with their own eyes that it contradicts.

## 6. Boundaries between close files

When two systems sit close enough to write over each other (two similar classes, two currencies, two enhancement systems), put a **boundary table at the top of both files**, identical text. Add a last row that makes it machine-checkable:

```markdown
| **Words banned in this file** | "intercept" · "shield" | "signal" · "command" |
```

```bash
# Is the boundary still holding?
grep -c "intercept" the-file-that-bans-it.md
```

A boundary that cannot be checked by a machine is a boundary that disappears within three months.

## 7. Renumbering or renaming without breaking the vault

1. **Count the inbound links first:** `grep -rl "\[\[old-name" | wc -l`.
2. **Above about 10 files, ask whether it is worth it.** A wrong name with complete links beats a right name with broken ones.
3. **Change it with one script across the vault**, never file by file.
4. **Run the link check immediately after** and report the numbers before and after.

## 8. Every file ends with two sections

```markdown
## Open questions
| Question |
|---|
| [UNDECIDED: ...] |

## Alternatives considered and rejected
| Alternative | Rejected because |
|---|---|
```

The second section matters more than people think. It stops someone proposing the same thing six months later, and it shows whether the author understood the trade-off or listed everything they liked. When research rejects something, it goes in this table with the reason.

## 9. Done means

| | Check |
|---|---|
| 1 | **Zero broken links**, file links and heading links |
| 2 | **Front matter matches the real marker count** in every touched file |
| 3 | **Nothing new makes a sentence in an old file false.** Its negation was searched. |
| 4 | **The rule just written exists nowhere else**, or a home was chosen |
| 5 | **Every number is tagged** `[PROVISIONAL: ...]` or justified |
| 6 | **"Alternatives considered and rejected" exists** with real reasons |
| 7 | **Index, map and task board updated** if a count or the layout changed |

## 10. Forbidden in Phase B

| Never | Because |
|---|---|
| **Force the standard layout over the one in use** | Right file names in exchange for a vault of broken links |
| **Compress a registry file to fit the 1 to 3 page rule** | A registry is long because it holds many things. Compressing it deletes data. |
| **Decide for the owner because "it is obvious"** | Obvious to a reader of the document may contradict a reason the owner never wrote down |
| **Edit old text quietly while writing new text** | The owner will not know what changed. Editing is allowed; every edit is reported. |
| **Create a new file because the old one "does not fit"** | Count the inbound links first. The answer is almost always edit, not create. |
