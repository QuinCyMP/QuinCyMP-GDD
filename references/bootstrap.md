# Phase A: starting from zero

Read this file only when the project has no design folder, or fewer than 5 files. Phase B skips it entirely and reads `living-vault.md` instead.

Everything else in the document is a consequence of five decisions. Writing before they are locked means rewriting the whole set later. So lock them first, and only then scaffold.

## 1. Lock five things

Do not write a file until the user has answered all five. Interview in **rounds**: ask every question whose prerequisites are already settled, number each one, and give your recommended answer under it. Wait for the answers, then ask the next round. Never fire twenty questions at once. When an answer is vague, offer 2 or 3 specific options and continue from the one chosen. Facts (what a comparable game does, what a genre's numbers look like) are yours to find; decisions are the user's.

**Lock 1. The 30-second core loop.** What the player presses, what responds, what they gain, and why they do it again, told as actions, not system names. "Fight, loot, upgrade" fails: it does not say how many seconds one fight takes, what the player decides during it, or how the loot changes the next fight.

**Lock 2. The One Thing.** One sentence in this shape:

> "In this game the player can ___, which [2 or 3 real games] cannot, because their systems ___."

If the sentence cannot be completed, the game has no reason to exist and the document will not sell. One is enough; two or more means the choice has not been made.

**Lock 3. Why other players are necessary.** Remove every other player. If the game is still as much fun, it is a single-player game with strangers running past. Name the systems that *need* other players: an economy needs producers and buyers, content needs groups, meaning comes from competition or reputation, the world changes through collective action. This is where amateur MMO documents break most often.

**Lock 4. A target player who exists.** Not "MMO fans aged 18 to 35" but "someone currently playing [real game] who quit because of ___". Every kind of buyer asks this, and a specific answer is what separates a document that sells from one closed on page two.

**Lock 5. A vertical slice one person could prove.** The smallest piece that makes The One Thing felt: how big, how many months, what is cut. Even if the user never builds it, it belongs in the document, because buyers use it to judge whether the design is provable or just an idea.

Completion criterion: all five written down in the user's words, each with its rejected alternatives.

## 2. Scaffold the document set

This layout is a proposal, not an order. A project that already has its own structure keeps it. Wrong file names with complete links beat right names with a vault of broken links.

```bash
python scripts/scaffold_gdd.py <target folder> --title "Game name"
```

The result:

```
design/
├── 00-one-pager.md        One page. The first file a stranger ever sees.
├── 01-vision.md           Pillars, The One Thing, target player, why multiplayer
├── 02-core-loops.md       Moment, session, week and lifetime loops
├── 03-world.md            World size, density, traversal, zoning
├── 04-progression.md      Levels, skills, gear, vertical versus horizontal
├── 05-combat.md           Pacing, numbers, roles, decisions per second
├── 06-economy.md          Faucets, sinks, player market, price tables
├── 07-social-mmo.md       Server topology, guilds, grouping, anti-griefing
├── 08-endgame-liveops.md  Hour 300 and who makes the content after that
├── 09-monetization.md     Revenue model and what it does to the design
├── 10-art-audio.md        Visual and audio direction plus the asset budget
├── 11-tech-assumptions.md What this design demands from engine and server
├── 12-scope-roadmap.md    Vertical slice, cuts, build order
├── 13-risks.md            Risks ranked by impact, with mitigations
├── GLOSSARY.md            Every in-game name, English first
├── data/                  CSV tables: xp curve, items, drop rates, prices, skills
└── pitch/
    ├── pitch-deck-outline.md
    └── buyer-brief.md     One per buyer type (see pitch.md)
```

Every generated file carries the standard headings, an `[UNDECIDED: ...]` marker per section, and an `open-questions:` count in its front matter, so gaps stay visible and countable. The script never overwrites an existing file.

Not every file needs writing in one sitting. Ask which file the user wants first. The order that works is `01 → 02 → 12 → 06` (vision, core loops, scope, economy): these four force the hardest decisions early. Write `00-one-pager.md` **last**. A page that summarises undecided things cannot be written.

Completion criterion: the folder exists, the user has picked the first file, and `GLOSSARY.md` has its first entries.

## 3. The constraint talk, once

An open-world MMORPG is the most expensive kind of game humans make. One person cannot finish one, not for lack of skill but because the genre needs a **content factory** that feeds players faster than they consume. Say this once, at the start, then stop.

Three real paths exist. The document should pick one on purpose:

- **Design in full, then sell or hand the design to a larger team.** The document must be complete enough for others to build from.
- **Shrink the scope to what a small team can ship.** A small MMO with a ceiling of 100 to 500 players, one world rather than shards, player-made content, systemic rather than handcrafted. Record this in `12-scope-roadmap.md` as the fallback plan, because it is what makes the vertical slice real.
- **Prototype The One Thing first, then find a team.** Adds the most value to the document of the three.

After the user has chosen, treat the constraint as acknowledged. From then on the job is to make their idea the best version of itself, not to repeat the feasibility warning every time they propose something new.
