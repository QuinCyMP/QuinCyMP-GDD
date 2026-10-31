---
name: quincymp-gdd
description: Write and maintain game design documents that record decisions, not dreams. Use when the user wants to design a game, write or audit a GDD, define a core loop, balance an in-game economy, design classes or skills, size an open world, plan progression or endgame, scope a project, or pitch a game to a publisher, buyer or co-founder. Strongest for MMORPG and open-world design, usable for any genre. Not for engine choice or gameplay code; this skill stops at the design.
---

# Game design doc

A design document is a record of decisions, not a description of dreams. Every section answers four questions: **what was decided, why, which alternatives were rejected, and what the numbers are**. A section that cannot answer all four is not designed yet. Write `[UNDECIDED: <the question to answer>]` in its place instead of covering the gap with prose. A declared gap earns more trust from a professional reader than false confidence, and a reader who buys designs spots the difference on page two.

Compare:

> Rejected: "The world is vast, with dynamic weather, and players explore freely."
>
> Accepted: "The world is 6 km². At 4.5 m/s a player crosses it in 9 minutes and meets a point of interest every 40 to 60 seconds of travel. This size was chosen because one person can hand-build 40 landmarks in 8 months. A 25 km² world was rejected: it leaves a landmark every 4 minutes, which reads as empty."

## Start

Decide the phase first. Then open a todolist with one entry per step of that phase and work it in order.

| | Phase A: starting from zero | Phase B: extending an existing vault |
|---|---|---|
| Signal | No design folder, or fewer than 5 files | Dozens of files that already link to each other |
| Job | Settle the big decisions: core loop, The One Thing, scope | Go deep per system without making an old file false |
| Risk | Beautiful prose with no decisions | A new decision that contradicts one already made |
| Read | [`references/bootstrap.md`](references/bootstrap.md) | [`references/living-vault.md`](references/living-vault.md) before touching any file |

In Phase B never impose the standard file layout on a project that already has its own. A layout that is in use and fully linked beats a standard one that needs 80 files rewritten to match. The five locks in `bootstrap.md` still have to be answerable, but if the project already answered them, read the answers instead of asking again.

## Rules for every file

**Names.** Prose in the team's working language. Every name of a thing in the game in English: stats, classes, jobs, currencies, systems, titles, items, gods, places. Those names get typed into code, databases and UI, so the document must use the names the code will use. Never coin a native-language word for an in-game thing. It reads well, nobody types it into a codebase, and it translates back three different ways until the team calls one thing by three names. Introduce a name once with a translation in parentheses, then use the English name alone: "**Glory** (honor) is the second currency", and from then on just `Glory`. Keep a `GLOSSARY.md` from the first file, English names first, explanations second, and update it whenever a name is created.

**Numbers.** Every system carries at least one real number. An unknown number gets an estimate tagged `[PROVISIONAL: 1,500 g/hr]`. A declared estimate can be argued with and fixed; an omission cannot. Numbers a document may not skip: TTK, session length, income per hour, players visible in one area, hours to endgame.

**Tables.** A table a human reads to understand a decision (comparing options, summarising rules) stays in the document, because a reader should not open two files to understand one thing. A table a machine imports (xp curve, drop rates, prices, per-item stats, dozens of rows) lives in `data/*.csv`. Do not create `data/` before real numbers exist; an empty folder waiting for numbers is debt, not structure.

**Length.** Measure decision density, not pages. Concept files (vision, core loops, one-pager) run 1 to 3 pages and are read in one sitting; longer means a choice has not been made. Registry files (classes, gods, stats, items) run as long as the list; a 27-job registry at 1,000 lines is correct, and shortening it deletes data. Rules files may be long but open with a "where to start" box. The test: read 10 random lines from the middle of a file; if none is a decision, that file is description. Fear repetition, not length. A rule that appears in three files gets one home and two links (see `living-vault.md`).

**Design before production.** Design files hold game numbers: world size, TTK, drop rate, concurrency. Production constraints (time, cost, head count, technical feasibility) live in one place, the scope file (`12-scope-roadmap.md` in the standard layout, or whatever the project calls it), and the user is told where they were recorded. An idea cut for "no time" before it was finished was never evaluated. Scope can shrink on any day; the right concept is found once, at the start.

**Team size is project data, not a default.** Read it from the project (its `CLAUDE.md`, a decision record, the scope file) before applying any "small team" advice in the references. If the project declares an enterprise or AAA team, team size is never a reason to cut an idea in a concept file, and the small-team advice is an option, not a limit.

**Rejections.** Every file ends with a section "Alternatives considered and rejected" with a reason per row. It is what separates a designer from a dreamer, and the section a professional buyer reads first, because it shows whether the author understands trade-offs or listed everything they like.

## Amateur signals in an MMORPG document

None of these is banned. Each is a default everybody writes, so including one without a reason announces that the section is not designed yet. When the user proposes one, do not refuse it. Ask the question in the right column and write the answer into the document. The answer is the design.

| Proposal | Why it is a warning sign | Ask |
|---|---|---|
| Warrior, mage, rogue, healer | Classes come from the player's fantasy, not from a template | Who does this class let the player *feel* like, and what decision does it make that no other class can? |
| Elves, dwarves, orcs | Not wrong, but free of content | How does the race change *play*? If only looks, cut it. |
| "A vast world" with no number | World size is a production constraint, not a slogan | How many km², built by whom, in how long? |
| Crafting as "combine materials, press button" | Labor, not a game | What does the player decide mid-craft, and do two players crafting the same item get different results? |
| Level 1 to 60, then repeat bosses | Needs a content factory feeding it forever | How much content can this team ship per month, and how much does endgame consume per month? |
| "AI-driven living NPCs" | Marketing until the decisions are named | What does an NPC decide, and how does a player notice within 5 minutes? |
| "Player-driven economy" | The system that breaks most easily | Where does money enter, where does it leave, at what rates, and what happens when bots arrive? |
| PvP, PvE, crafting, housing and pets, all of it | Everything means nothing was chosen | If one system had to survive, which one, and when does the next one arrive? |

## References

Read the file that matches the section being written. Do not read them all at once.

| Read | When |
|---|---|
| [`references/bootstrap.md`](references/bootstrap.md) | Phase A only. The five locks, the question rounds, the document set and scaffold, the constraint talk. Phase B skips this file. |
| [`references/document-structure.md`](references/document-structure.md) | Starting any standard file, or unsure what a section must contain. Per-file requirements and the questions to ask. |
| [`references/living-vault.md`](references/living-vault.md) | Phase B, before touching any file. Single home, machine-readable markers, link checks, contradiction hunting, boundary tables, renames. |
| [`references/classes-and-skills.md`](references/classes-and-skills.md) | Any ability the player chooses: classes, jobs, build paths, skills, perks. The verb count, the five criteria, the nine prohibitions, the four research shelves, slots versus library. |
| [`references/economy.md`](references/economy.md) | File 06, file 04, or any table in `data/`. Faucet and sink, drop rate and pity, xp curves, power ratios, market liquidity, time as currency. |
| [`references/world.md`](references/world.md) | File 03, or any talk of world size, maps, exploration, travel. |
| [`references/roguelike.md`](references/roguelike.md) | Roguelike or roguelite runs. Run length, encounter structure, resets, persistent progression, seeds, replay and difficulty scaling. |
| [`references/mmo-systems.md`](references/mmo-systems.md) | Files 04 to 09 in an MMO. Server topology, concurrency, progression, social glue, endgame consumption, anti-cheat, onboarding. |
| [`references/pitch.md`](references/pitch.md) | Any file under `pitch/`, or the user asks about selling, publishers, rights. |

## Delivery checklist

Before reporting a document done, run every test. Fix the failures first.

1. **Stranger test.** Someone who never spoke to the user reads the one-pager (`00-one-pager.md` in the standard layout) and can explain the game to a friend correctly.
2. **Programmer test.** There are enough numbers to start coding at least one system without asking a question.
3. **Distinctiveness test.** With the title removed, a reader can still tell this apart from a generic MMO.
4. **Rejection test.** Every file has a real "Alternatives considered and rejected" section with reasons.
5. **Honesty test.** Every unknown is marked `[UNDECIDED: ...]` or `[PROVISIONAL: ...]`, not covered with prose.
6. **Contradiction test** (Phase B). Nothing just written makes a sentence in an older file false. If it does, fix the source, never leave two files disagreeing.
7. **Single-home test** (Phase B). The rule just written does not already exist elsewhere; if it does, one home was chosen and the rest link to it.

Test 5 matters most in Phase A. Test 6 matters most in Phase B. A document that admits what it does not know is one people dare to build on; a document that contradicts itself is one nobody trusts anywhere.

## Final response

Report the decisions made, the count of `[UNDECIDED]` markers per file, and in Phase B every sentence in an older file that was changed and why. Do not restate the document.
