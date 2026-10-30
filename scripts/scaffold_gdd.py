#!/usr/bin/env python3
"""Scaffold a game design document set with standard headings and empty CSV tables.

Usage:
    python scaffold_gdd.py <target folder> --title "Game name"
    python scaffold_gdd.py ./design --title "Rustfall" --only 01,02,12,06
    python scaffold_gdd.py ./design --title "Lantern Run" --genre roguelike

Every generated file carries the standard headings, one [UNDECIDED: ...] marker
per section so gaps stay visible instead of hidden behind prose, and an
`open-questions:` count in its front matter that matches the marker count.

The script never overwrites an existing file. Re-running it is safe.
"""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

TODO = "[UNDECIDED: {}]"

# slug -> (file title, [(section heading, leading question to answer)])
DOCS = {
    "00-one-pager": ("One-pager", [
        ("Logline", "One sentence: genre + difference + what the player does"),
        ("What this game is", "Three paragraphs, four lines each at most"),
        ("Why it is different", "The One Thing, compared with two real games"),
        ("Why anyone will play it", "What the target player plays now, and what frustrates them"),
        ("The numbers", "world size / session length / time to endgame / concurrency"),
        ("Status and the ask", "What exists, and what is wanted from the reader"),
    ]),
    "01-vision": ("Vision", [
        ("Pillars", "Three decision rules sharp enough to refuse good things"),
        ("The One Thing", "In this game the player can ___, which [real game] cannot, because ___"),
        ("Target player", "What they play now, what frustrates them, minutes per session"),
        ("Why other players are needed", "Which system breaks at once when played alone"),
        ("Target emotion", "Minute 10 / hour 10 / hour 100"),
    ]),
    "02-core-loops": ("Core loops", [
        ("Moment loop (1 to 30 seconds)", "What is pressed, what responds, what is decided"),
        ("Session loop (20 to 90 minutes)", "What is done first after logging in, and when quitting feels earned"),
        ("Week loop", "What brings the player back tomorrow that is not a daily quest"),
        ("Lifetime loop", "What finished means, and what exists after it"),
    ]),
    "03-world": ("World and exploration", [
        ("Size and travel time", "km² / speed in m/s / time to cross"),
        ("Density", "Target spacing of points of interest, and their count per kind"),
        ("Traversal", "Travel verbs and their effect on the world's shape"),
        ("Fast travel", "Yes or no, how it unlocks, what it costs"),
        ("Zoning and gating", "Level / skill / knowledge gates"),
        ("How this team builds the world", "Modular kit / procedural plus landmarks / a world players change"),
    ]),
    "04-progression": ("Progression", [
        ("Sources of progress", "Level / gear / skills / player knowledge / reputation"),
        ("Vertical or horizontal", "Which, and who feeds the content"),
        ("The cap and after it", "Is there a cap, and how does a player grow past it"),
        ("A new player in year two", "Do they catch up, and should they"),
        ("Numbers", "Hours to cap / endgame-to-new-player power ratio, see data/xp-curve.csv"),
    ]),
    "05-combat": ("Combat", [
        ("Form", "Tab-target or action, and the reason, tied to concurrency"),
        ("Rhythm", "GCD / buttons actually used / decisions per second"),
        ("Numbers", "TTK per mob / TTK player versus player"),
        ("Roles and dependence", "If roles exist, why one player cannot cover them all"),
        ("Death", "What is lost, and how long the return takes"),
    ]),
    "06-economy": ("Economy", [
        ("Faucets", "Where currency enters, g/hr each, see data/economy-flow.csv"),
        ("Sinks", "Where currency leaves, g/hr each"),
        ("Balance", "faucet minus sink per month, as a percentage"),
        ("Player market", "Bound or not / where trade happens / fee / minimum population for liquidity"),
        ("Time as currency", "Hours each important item costs"),
        ("Bot risk", "Which activities a bot does better than a human, and the defence"),
    ]),
    "07-social-mmo": ("Social and MMO structure", [
        ("Server topology", "Shard / megaserver / single shard / instanced, and the reason"),
        ("Concurrency", "Players per area / target CCU"),
        ("Why strangers cooperate", "The mechanism that forces or rewards dependence"),
        ("Grouping and guilds", "What a guild can do that a friend group cannot"),
        ("Anti-griefing and reputation", "Who enforces it: the system or players"),
        ("Critical mass", "Minimum players per system, and how it degrades below that"),
    ]),
    "08-endgame-liveops": ("Endgame and live ops", [
        ("After 300 hours", "The primary endgame form"),
        ("Production versus consumption", "What the team ships per month versus what a heavy player consumes"),
        ("Content players make for each other", "Which systems players fill themselves"),
        ("Update cadence", "Every how many weeks, by whom"),
    ]),
    "09-monetization": ("Monetization", [
        ("Model", "B2P / subscription / F2P, and the reason"),
        ("Effect on the design", "What this model forces the design to do differently"),
        ("What will never be sold", "The line not crossed, and why"),
        ("Numbers", "Price / plausible ARPU / server break-even point"),
    ]),
    "10-art-audio": ("Art and audio", [
        ("Visual style", "Chosen because this team can produce it"),
        ("Technical budget", "Asset count for the vertical slice / texture sets / modular kit"),
        ("Audio", "Minimum track count and SFX count"),
        ("Source of every reference image", "Required before the document reaches a buyer"),
    ]),
    "11-tech-assumptions": ("Tech assumptions the design demands", [
        ("Players visible in one area", "How many"),
        ("Tick rate the combat needs", ""),
        ("Data that must persist", "Inventory / land / relationships / world state"),
        ("Server decides, client decides", "Anything convertible to value is server-only"),
        ("World loading", "Streaming / zones / instances"),
    ]),
    "12-scope-roadmap": ("Scope and roadmap", [
        ("Vertical slice", "The smallest thing that proves The One Thing: area, systems, assets, time"),
        ("Build order", "Which system comes first because others depend on it"),
        ("Cut from version one", "With the condition for bringing each back"),
        ("Fallback if scope shrinks", "What a 100 to 500 player MMO version looks like"),
    ]),
    "13-risks": ("Risks", [
        ("Risk table", "Sorted by impact × likelihood, with early warnings and mitigations"),
    ]),
}

PITCH = {
    "pitch-deck-outline": ("Pitch deck outline", [
        ("Slides 1 to 11", "See references/pitch.md. Do not forget the ask slide."),
    ]),
    "buyer-brief": ("Buyer brief", [
        ("Who the recipient is", "A publisher or investor / B studio or IP buyer / C co-founder"),
        ("The question in their head", ""),
        ("What to emphasise", ""),
        ("What to leave out", ""),
    ]),
}

CSV_HEADERS = {
    "xp-curve.csv": ["level", "xp_required", "xp_cumulative", "est_hours", "est_hours_cumulative"],
    "items.csv": ["id", "name", "tier", "slot", "power", "value_g", "bind", "source"],
    "drop-tables.csv": ["mob_id", "item_id", "drop_rate", "min_qty", "max_qty", "pity_after"],
    "mob-stats.csv": ["id", "name", "level", "hp", "dps", "xp_reward", "gold_reward", "ttk_seconds"],
    "skills.csv": ["id", "name", "class", "cooldown", "cost", "damage_coeff", "unlock_level"],
    "economy-flow.csv": ["source_type", "name", "gold_per_hour", "player_level_band"],
}


# The MMO preset uses DOCS unchanged. Roguelike replaces genre-specific questions
# and omits social/live-ops files while retaining shared art, pitch and risk work.
ROGUELIKE_SECTIONS = {
    "00-one-pager": [
        (heading, "Run length / encounters per run / time to first victory / replay goals"
         if heading == "The numbers" else prompt)
        for heading, prompt in DOCS["00-one-pager"][1]
    ],
    "01-vision": [
        ("Why replay", "What makes another run worth starting after victory or defeat")
        if heading == "Why other players are needed" else (heading, prompt)
        for heading, prompt in DOCS["01-vision"][1]
    ],
    "02-core-loops": [
        ("Moment loop", "What is pressed, what responds, what is decided"),
        ("Encounter loop", "Choices per encounter / rewards / recovery between encounters"),
        ("Run loop", "Minutes per run / route choices / win and loss conditions / save and quit rules"),
        ("Replay loop", "What changes between runs, what resets, and why another attempt is different"),
    ],
    "03-world": [
        ("Run map", "Rooms or nodes per run / route length / branching choices"),
        ("Encounter distribution", "Combat / rest / reward / event counts and placement constraints"),
        ("Generation", "Hand-authored / procedural / hybrid, and safeguards against unwinnable routes"),
        ("Traversal and gates", "Movement verbs / backtracking / information revealed before choosing a route"),
    ],
    "04-progression": [
        ("Within a run", "How power grows through items, skills and player choices"),
        ("Between runs", "Knowledge / unlocks / permanent power, and why each persists"),
        ("Reset rules", "Exactly what death, victory and abandoning a run erase or preserve"),
        ("Unlock pacing", "Runs to first unlock / hours to full option library / beginner-to-veteran power ratio"),
        ("After the first victory", "Difficulty tiers / alternate routes / mastery goals, with numeric targets"),
    ],
    "05-combat": [
        ("Form", "Turn-based or real-time, and the reason tied to player decisions"),
        ("Rhythm", "Decisions per turn or second / encounter duration"),
        ("Numbers", "Enemy health / player damage / expected turns or seconds to defeat an enemy"),
        ("Build boundaries", "What each build does well, what it cannot do, and counters"),
        ("Failure", "Damage and recovery budget across a run / what a loss teaches"),
    ],
    "06-economy": [
        ("Run resources", "Currency and consumables gained per encounter and spent per run"),
        ("Shops and rewards", "Prices / reward choices / reroll and removal costs"),
        ("Scarcity", "Expected budget at each stage and the choices it forces"),
        ("Carry-over", "Which resources survive a run and why; reject carry-over if it removes scarcity"),
    ],
    "09-monetization": [
        ("Model", "Premium / paid expansions / other, and its effect on a complete run"),
        ("What will never be sold", "Which power and replay advantages stay outside the store, and why"),
        ("Numbers", "Price / expected revenue per sale / sales needed to break even"),
    ],
    "11-tech-assumptions": [
        ("Run state", "Seed / map / inventory / enemies / unlocks that must persist"),
        ("Save and resume", "Save frequency / rollback limit / behavior after a crash"),
        ("Simulation", "Turn or update budget / maximum active enemies / deterministic replay needs"),
        ("Loading", "Room transitions / run generation time / maximum loading pause"),
    ],
    "12-scope-roadmap": [
        (heading, "The smallest complete run: rooms / enemies / builds / replay variation"
         if heading == "Fallback if scope shrinks" else prompt)
        for heading, prompt in DOCS["12-scope-roadmap"][1]
    ],
}


def genre_docs(genre):
    if genre == "mmo":
        return DOCS
    return {
        slug: (title, ROGUELIKE_SECTIONS.get(slug, sections))
        for slug, (title, sections) in DOCS.items()
        if slug not in {"07-social-mmo", "08-endgame-liveops"}
    }


def render(title: str, game: str, sections, slug: str) -> str:
    lines = [
        "---",
        f"open-questions: {len(sections)}",
        "---",
        f"# {title}",
        "",
        f"> Game: **{game}** · last updated {date.today().isoformat()}",
        "",
    ]
    for heading, prompt in sections:
        lines.append(f"## {heading}")
        lines.append("")
        if prompt:
            lines.append(f"<!-- Answer: {prompt} -->")
            lines.append("")
        lines.append(TODO.format(prompt or heading))
        lines.append("")
    if slug != "00-one-pager":
        lines += [
            "## Alternatives considered and rejected",
            "",
            "| Alternative | Rejected because |",
            "|---|---|",
            "| | |",
            "",
        ]
    return "\n".join(lines)


def write_if_absent(path: Path, content: str, created: list, skipped: list) -> None:
    if path.exists():
        skipped.append(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(path)


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a game design document set")
    ap.add_argument("target", help="target folder, for example ./design")
    ap.add_argument("--title", required=True, help="game name")
    ap.add_argument("--only", help="generate only these numbered files within the genre preset, for example 01,02,12,06")
    ap.add_argument("--genre", choices=("mmo", "roguelike"), default="mmo",
                    help="question and file preset (default: mmo; roguelike: single-player runs)")
    args = ap.parse_args()

    root = Path(args.target)
    created: list = []
    skipped: list = []

    # Strip leading zeros on both sides: some shells (PowerShell) turn 01 into 1.
    wanted = None
    if args.only:
        wanted = {p.strip().lstrip("0") or "0" for p in args.only.split(",") if p.strip()}

    for slug, (title, sections) in genre_docs(args.genre).items():
        if wanted and (slug.split("-")[0].lstrip("0") or "0") not in wanted:
            continue
        write_if_absent(root / f"{slug}.md", render(title, args.title, sections, slug), created, skipped)

    if not wanted:
        for slug, (title, sections) in PITCH.items():
            write_if_absent(root / "pitch" / f"{slug}.md", render(title, args.title, sections, slug), created, skipped)

        glossary = "\n".join([
            "# Glossary",
            "",
            f"> Game: **{args.title}** · every in-game name, English first.",
            "",
            "| Name | Meaning | Avoid |",
            "|---|---|---|",
            "| | | |",
            "",
        ])
        write_if_absent(root / "GLOSSARY.md", glossary, created, skipped)

        for name, headers in CSV_HEADERS.items():
            if args.genre == "roguelike" and name in {"xp-curve.csv", "economy-flow.csv"}:
                continue
            path = root / "data" / name
            if path.exists():
                skipped.append(path)
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8", newline="") as fh:
                csv.writer(fh).writerow(headers)
            created.append(path)

    for p in created:
        print(f"created  {p}")
    for p in skipped:
        print(f"skipped  {p} (exists)")
    print(f"\n{len(created)} created, {len(skipped)} skipped")
    if created:
        print("Suggested writing order: 01 -> 02 -> 12 -> 06, then the rest. Write 00 last.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
