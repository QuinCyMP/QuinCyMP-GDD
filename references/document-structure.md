# Document structure, file by file

Read this when starting a standard file, or when unsure what a section must contain. Each entry below lists **what the file must have** and **what to ask the user to get it**. Files 03, 06 and 07 are owned by their own references and only pointed at here.

Contents: [00 One-pager](#00-one-pager) · [01 Vision](#01-vision) · [02 Core loops](#02-core-loops) · [03 World](#03-world) · [04 Progression](#04-progression) · [05 Combat](#05-combat) · [06 Economy](#06-economy) · [07 Social and MMO](#07-social-and-mmo) · [08 Endgame and live ops](#08-endgame-and-live-ops) · [09 Monetization](#09-monetization) · [10 Art and audio](#10-art-and-audio) · [11 Tech assumptions](#11-tech-assumptions) · [12 Scope and roadmap](#12-scope-and-roadmap) · [13 Risks](#13-risks)

## 00 One-pager

Written last. It is the only file a stranger reads, and 80% of them read nothing else. One real A4 page; longer means it has not been condensed.

```
# <Game name>
<One-sentence logline: genre + difference + what the player does>

**Genre** · **Platform** · **Target player** · **Revenue model** · **Current status**

## What this game is
Three paragraphs, four lines each at most.

## Why it is different
The One Thing, compared with two real games.

## Why anyone will play it
What the target player plays now, and what frustrates them.

## The numbers
World size · session length · time to endgame · concurrency per zone.

## Status and the ask
What exists, and what is wanted from the reader (team, money, publisher, buyer).
```

Logline, rejected and accepted:

> Rejected: "An open-world fantasy MMORPG where players adventure through a vast world."
>
> Accepted: "An MMORPG where everything players build decays in real time, so the world belongs to whoever still maintains it, not whoever arrived first."

## 01 Vision

Must have:

- **Three pillars.** Decision rules that answer "does this feature belong?" and are sharp enough to *refuse* good things. A pillar that refuses nothing ("fun", "quality") is not a pillar.
- **The One Thing** in the comparison sentence from `bootstrap.md`.
- **Target player.** What they play now, what frustrates them, how long a session lasts.
- **Why other players are needed.** Which system breaks when played alone.
- **Target emotion** at minute 10, hour 10 and hour 100.

Ask the user:

- Which game made you think "if only it did this instead"?
- If everything but one system were cut, which stays?
- How does a player describe this game to a friend in one sentence?

A pillar that works:

> **"Everything decays."** No permanent item, base or rank.
> Refuses: legendary items kept forever, permanent achievements, land bought once and owned forever.

## 02 Core loops

Four layers, each with a real duration:

| Layer | Duration | Must answer |
|---|---|---|
| **Moment** | 1 to 30 seconds | What is pressed, what responds, what is decided |
| **Session** | 20 to 90 minutes | What the player does first after logging in, and when quitting feels earned |
| **Week** | 5 to 15 hours | What brings them back tomorrow that is not a daily quest |
| **Lifetime** | 100 to 1,000 hours | What "finished" means, and what exists after it |

Write each layer as a **sequence of real actions**, not system names:

> Rejected: "The player fights, loots, upgrades, fights again."
>
> Accepted: "Three mobs ahead. Pull one at a time (safe, 25 seconds) or the group (risky, 12 seconds, bonus loot from the multi-kill). The decision repeats every 20 seconds and shifts with remaining HP."

Every loop contains a decision the player makes. A loop with no decision is labor.

## 03 World

Owned by [`world.md`](world.md).

## 04 Progression

Answer four questions:

1. What makes the player stronger: level, gear, skills, the player's own knowledge, reputation in the world?
2. **Vertical or horizontal.** More power (needs new content forever) or more options (far more buildable for a small team)?
3. Is there a cap, and how does a player grow after reaching it?
4. Does a player who joins in year two catch up, and *should* they?

Numbers required: the xp curve (`data/xp-curve.csv`), hours to the last level, the power ratio between a new player and endgame.

Small-team trap: vertical progression needs a new tier every 3 to 6 months or players run out of goals. Without a content team, lean horizontal plus prestige that players give meaning to themselves.

## 05 Combat

Numbers, or it is not designed:

- **TTK.** Seconds to kill a normal mob, and seconds player versus player.
- **GCD and rhythm.** How often a button can be pressed, and how many buttons a real fight uses.
- **Decisions per second.** Slow (tab-target, planning) or fast (action, reflex). This single choice decides the whole netcode.
- **What death means.** What is lost, and how long the walk back is.

The deciding MMO question is **tab-target or action combat**. Action needs a high tick rate, multiplies server cost and caps players per area. Tab-target tolerates latency, supports more players, and is why the large MMOs still use it. Write the reason for the choice down; the first question from whoever builds this is that one.

## 06 Economy

Owned by [`economy.md`](economy.md).

## 07 Social and MMO

Owned by [`mmo-systems.md`](mmo-systems.md).

### Co-op for 2 to 4 players

For a small co-op game, answer these questions instead of assuming a public MMO population. Record the chosen rule, its reason, a rejected alternative and a measurable limit for each row.

| Decision | Questions to answer | Illustrative example, not a default |
|---|---|---|
| Why a second player matters | Which interaction needs another person? Is solo play supported, and what changes at each party size? | Two players carry a heavy object; a solo player uses a slower cart. Reject a mandatory partner if solo completion is promised. |
| Drop-in and drop-out | When can someone join or leave? What happens to encounter difficulty, rewards and their inventory? | Join at a checkpoint within 2 minutes; rescale the next encounter. Reject immediate rescaling if leaving would trivialise a boss. |
| Shared or split progression | Who owns world unlocks, character upgrades and loot? How does an absent friend catch up? | World gates are shared; equipment is personal; a returning player catches up within 1 session. Reject independent gates if they prevent friends regrouping. |
| Host departure and migration | Does play stop, resume from a shared save, or migrate live? Who may host next, and how much progress can be lost? | Resume from a checkpoint at most 60 seconds old. Reject live migration if interruption is acceptable to the design. |

A shared save and seamless host migration are different promises. [Grounded's Shared Worlds announcement](https://grounded.obsidian.net/news/grounded/grounded-heads-into-the-home-stretch) describes cloud worlds that friends can host while the original host is offline. Use that distinction to choose the player experience before recording persistence and networking requirements in file 11.


## 08 Endgame and live ops

The one question that matters: **after 300 hours, what does a player log in to do?**

Real options (more than one is fine, but name the primary one):

| Form | Demands from the team | Small-team fit |
|---|---|---|
| New raid or dungeon tier | New content every 2 to 3 months | Most expensive |
| Competitive or ranked PvP | Continuous balance plus anti-cheat | Balance eats time |
| Economy and trade | Tuning numbers, no new assets | Good |
| Politics, territory, guild war | Systems built once, players make the drama | Best value |
| Housing and creation | Building tools plus storage | Good if the tools are good |
| Procedural or roguelike repeats | Well-designed randomness | Good |

State the **consumption rate**: a heavy player burns content that took 3 months to build in 2 weeks. Write that rate down and say what fills the gap.

## 09 Monetization

Pick one, **buy-to-play, subscription or free-to-play**, then write what it does to the design. A revenue model changes the design, not just the billing:

- **B2P.** No recurring revenue; needs DLC or cosmetics. Design so a player can quit satisfied.
- **Subscription.** Needs a steady content cadence or players cancel. Fits games whose economy must stay clean.
- **F2P.** The *moments people pay for* are designed from day one, not a shop bolted on later. Pay-to-win risk, which can destroy the player economy wholesale.

Write down **what will never be sold**. That line has sales value: it shows the author knows player trust is an asset.

## 10 Art and audio

Not just "which style". The file carries the **technical budget**, because that decides whether the team can ship:

- Asset count for the vertical slice (characters, mobs, props, armor sets).
- Constraints that speed production: texture set count, swappable color systems, a modular kit.
- A style chosen because *this team can produce it*. Stylized costs a fraction of realistic.
- Audio: minimum track count and SFX count.

## 11 Tech assumptions

The file that makes the document hand-over-able. It says what the design **demands** from the technical side without choosing an engine:

- Players that must see each other in one area (how many).
- Tick rate the combat system needs.
- Data that must persist: inventory, land, relationships, world state.
- What the server decides and what the client may decide. Anything convertible to value is server-only.
- World size and how it loads: streaming, zones, instances.

Write requirements, not solutions. Whoever builds it picks the method, but must know the limits.

## 12 Scope and roadmap

Three parts:

1. **Vertical slice.** The smallest thing that proves The One Thing: area, number of systems, asset count, time.
2. **Build order.** Which system comes first because others depend on it.
3. **Cut from version one**, with reasons and the condition for bringing each back.

Part 3 sells the document. It answers the buyer's question "what does the smallest version that is still this game cost?"

## 13 Risks

A table sorted by **impact × likelihood**, not by the order they came to mind:

| Risk | Impact | Likelihood | Early warning | Mitigation |
|---|---|---|---|---|

Risks every MMO document carries, because buyers look for them:

- Inflation breaks the economy; bots farm currency.
- Player count never reaches critical mass, so every system that needs crowds dies.
- Server cost per player exceeds revenue per player.
- Content production cannot keep up with consumption.
- The One Thing is not fun when tested. Always the biggest risk.

A document that states its risks plainly is more credible than an optimistic one. Buyers already know the risks exist; they are checking whether the author does.
