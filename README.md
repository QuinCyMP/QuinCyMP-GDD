# QuinCyMP GDD

An agent skill for Claude Code, Codex, OpenCode and other agents that write game design documents. The documents it produces record decisions, not dreams: every section says what was decided, why, which alternatives were rejected, and what the numbers are. Anything still open is marked `[UNDECIDED: ...]` so it can be counted and found.

Strongest for MMORPG and open-world design. Usable for any genre.

## What it does

| Task | What you get |
|---|---|
| Start a game from zero (Phase A) | Five decisions locked in question rounds before any file is written, then a 14-file document set with `GLOSSARY.md`, pitch files and CSV tables from `scripts/scaffold_gdd.py` |
| Extend a project that already has documents (Phase B) | Contradiction, link and single-home checks before anything new is added, so old files never silently become false |
| Design classes, jobs and skills | A verb count, five pass criteria, nine prohibitions, four research shelves, library versus slots, boundary tables between close classes |
| Balance an economy | Working formulas for faucets and sinks, drop rates and pity, xp curves, power ratios, market liquidity, time as currency |
| Size an open world | World size from density and travel time, points of interest by kind, traversal verbs, gating, how a small team builds a big world |
| Design MMO systems | Server topology, concurrency, progression, social glue, endgame consumption, anti-cheat, onboarding |
| Sell or hand over the design | Five real paths to market, three buyer briefs, the send order, rights in plain terms, an 11-slide deck outline |

## Install

Claude Code, for every project:

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD ~/.claude/skills/quincymp-gdd
```

Claude Code, one project:

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD .claude/skills/quincymp-gdd
```

Codex and other agents that read `.agents/skills/`:

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD .agents/skills/quincymp-gdd
```

With the [skills CLI](https://skills.sh):

```bash
npx skills add QuinCyMP/QuinCyMP-GDD
```

## Use

Talk to the agent as you would to a designer:

- "I want to make a survival MMO. Help me design the systems."
- "Write a GDD for this game."
- "Balance the damage." "Design the crafting system." "Design the classes."
- "Audit my design folder for contradictions."
- "Pitch this to a publisher."

The skill asks the questions it needs before writing, gives a recommended answer under each one, and marks every unanswered point in the document instead of covering it with prose.

Scaffold a document set by hand:

```bash
python scripts/scaffold_gdd.py ./design --title "Game name"
python scripts/scaffold_gdd.py ./design --title "Game name" --only 01,02,12,06
```

The script never overwrites an existing file and needs only Python 3.8 and the standard library.

Check an existing document set for broken wikilinks and inconsistent question counts:

```bash
python scripts/check_vault.py ./design
```

The checker reports file and line locations and exits non-zero on problems.
See [the living-vault reference](references/living-vault.md) for supported link forms.

## Layout

```
SKILL.md                      The process: phases, rules for every file, amateur signals, delivery checklist
references/
  bootstrap.md                Phase A: the five locks, the document set, the constraint talk
  document-structure.md       What each of the 14 files must contain, and what to ask to get it
  living-vault.md             Phase B: single home, markers, links, contradictions, boundaries, renames
  classes-and-skills.md       Classes, jobs and skills
  economy.md                  Economy math
  world.md                    Open world
  mmo-systems.md              MMO systems
  pitch.md                    Selling or handing over the design
scripts/
  scaffold_gdd.py             Scaffolds the document set, GLOSSARY.md and CSV tables
  check_vault.py              Checks wikilinks and open-question counts without changing files
agents/
  openai.yaml                 Display metadata for Codex
```

## Language

Prose is written in the team's working language. Every name of a thing in the game is English, because the names in the document must be the names in the code. The skill was first written for a Thai-speaking team and is now maintained in English.

## Credits

The structure of this skill follows two sets of skills whose authors publish them under MIT: [pstack](https://github.com/cursor/plugins/tree/main/pstack) by poteto (short `SKILL.md` with phases, a `references/` folder read on demand, a delivery checklist and a final-response section) and [Matt Pocock's skills](https://github.com/mattpocock/skills) (trigger-led descriptions, decisions interviewed in rounds, reference files linked with the condition for reading them). No text from either was copied.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues labelled `good first issue` are a fine place to start.

## Related

[dense-melee-lab](https://github.com/QuinCyMP/dense-melee-lab) is reproducible netcode research by the same author: single-server limits for dense melee, a replica tier on unmodified Netcode for Entities, and several deciders resolving one fight bit-identically. Read it when the `mmo-systems` reference asks how many players one server can hold.

## License

[MIT](LICENSE) · © 2026 QuinCyMP
