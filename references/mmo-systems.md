# MMO systems and the traps new documents fall into

Read when writing files 04 to 09. Every topic here is a decision that must come **before** the rest of the document, because MMO systems are coupled far more tightly than a single-player game's. Changing the server topology while writing file 08 means rewriting files 03 to 07.

Contents: [1 Server topology](#1-server-topology) · [2 Concurrency](#2-concurrency) · [3 Progression](#3-progression) · [4 Social](#4-social) · [5 Endgame and consumption](#5-endgame-and-consumption) · [6 Anti-cheat and bots](#6-anti-cheat-and-bots) · [7 Onboarding and critical mass](#7-onboarding-and-critical-mass) · [8 Done means](#8-done-means)

## 1. Server topology

Decide this before designing the world, because it decides which shapes the world can take.

| Model | What it is | Effect on design | Cost |
|---|---|---|---|
| **Shard, realm** | Several copies of the world, separate populations | Small communities that know each other, but friends on different shards is a problem | Cheapest, scales easily |
| **Megaserver** | One world, auto-layered by density | No dead servers, but "neighbours" never stay the same, which erodes community | Medium |
| **Single shard** | Everyone truly in one world | Politics, economy and territory carry the most meaning | Most expensive and hardest |
| **Instanced zones** | The world split into rooms | Easiest for a small team, but kills the open-world feel | Cheap |
| **Session-based** | A persistent world played in rounds | Buildable by a small team; not a full MMO | Cheapest |

Trap: new documents write "single shard, one world, everyone meets" because it sounds grand. It is the most expensive model in games (EVE Online runs a core team of hundreds to do it). Choosing it requires a written reason why this design *needs* it, not just wants it.

## 2. Concurrency

| Number | Decides |
|---|---|
| Players visible to each other in one area | Netcode, combat system, area size, event design |
| Players online at once across the game (CCU) | Server cost, matchmaking, market liquidity |
| Registered players in total | Community size, feasibility of crowd systems |

Working reference ranges:

- **20 to 50 per area.** Action combat and a high tick rate are possible.
- **100 to 200 per area.** Tick rate must drop; abilities must tolerate imprecision.
- **500+ per area.** Time dilation or queues; combat slows a lot.

A small team targets **30 to 60 per area** and makes that number feel "full" with smaller spaces. A small world with 40 players feels more alive than a large one with 400 spread out until nobody meets. Write it in the document as an advantage, on purpose, not as an apology.

## 3. Progression

**Vertical**: numbers grow (level 60 to 70, a 100-damage sword to 150).

- Pro: clear, measurable progress that brings players back.
- Con: **needs new content forever**, and old content turns to junk with every new tier.
- Hidden cost: every tier means new mobs, areas and gear. A factory.

**Horizontal**: options grow (new skill types, jobs, paths that are different, not stronger).

- Pro: old content stays alive, new players catch up, content does not expire.
- Con: much harder to balance, and "progress" is harder to feel.
- The path a small team should choose, with the reason written in the document.

A third path: **progression in the player, not the character**. The player gets better, learns the map, knows where the rare things are, knows people, has a reputation. Nearly zero content cost, but knowledge must be made genuinely valuable: a world with secrets, a market where information has a price, a reputation the system records.

Numbers required: hours to cap, the new-player to endgame power ratio, time for a new player to catch up.

## 4. Social

The question new documents skip, and the heart of an MMO: **why do two strangers cooperate instead of playing alone?**

Answers that work (pick at least one, then design the systems for it):

- **Mechanical dependence.** One player really cannot (a door needs two, a job makes what it cannot use).
- **Economic dependence.** Needed goods come only from other players.
- **Safety in numbers.** The world is dangerous enough that travelling alone is a risk.
- **Reputation and memory.** The system remembers who did what, so names must be protected.

Systems always designed together:

| System | Must answer |
|---|---|
| Grouping | How players find each other: browse, auto-match, post. The choice changes the whole community. |
| Guilds | What a guild *does* that a friend group cannot. No answer means the guild is a chat room. |
| Communication | Which chat channels, and whether proximity chat exists. Decides whether strangers talk. |
| Anti-griefing | What stops the strong preying on the weak, and who enforces it: the system or players. |
| Reputation and consequences | What a cheat or a betrayer loses. |

The large trap: systems that need crowds (40-player raids, guild wars, a liquid market) **die as a whole** below critical mass. For every such system the document states the **minimum player count at which it still works**, and how it degrades below that rather than simply breaking.

## 5. Endgame and consumption

The equation that belongs in the document:

```
content lifetime = content volume ÷ heavy-player consumption rate
```

Industry reference: the top 5% consume content **10 to 30 times** faster than a team can build it. A dungeon that took 2 months is played out in 1 to 2 weeks.

Solutions a small team can use, by value:

1. **Content players make for each other.** PvP, politics, economy, territory war. Build the system once; players fill it.
2. **Systems that differ every repeat.** Procedural, well-designed randomness, seasonal world states.
3. **Depth over breadth.** One system that can be mastered endlessly (fishing in FF14, trade in EVE).
4. **Accept that players take breaks.** Design for easy return at updates instead of trying to hold everyone forever.

Item 4 is the honesty a professional document has and a first document is afraid to write.

## 6. Anti-cheat and bots

The most forgotten topic, and the one that convinces a professional buyer the author knows the genre.

- **What the server decides.** The iron rule: anything convertible to value is decided by the server only. Damage, drops, movement that affects collision, every transaction.
- **Bot incentives.** Any repeatable activity with guaranteed income gets bots. Design income activities to need decisions or competition, and the incentive shrinks at the source.
- **RMT** (real-money trading of in-game currency). It always appears. Fight it to the death, or open a legal channel that drains the black market (EVE's PLEX).
- **Moderation cost.** Who bans, and how many hours per week.

## 7. Onboarding and critical mass

- **Time to first fun (TTFF).** Minutes until the player touches The One Thing. Target **under 10 minutes**. An MMO that has players kill rats outside town for 3 hours before the interesting part is dead before it starts.
- **When new players meet veterans.** Too early and they feel small; too late and they do not know others exist.
- **Does the game still work with 20 players online?** It must be answered, because launch day and the day the population thins look the same, and most MMOs die then, not when crowded.

## 8. Done means

The MMO part of the document is complete when every line has an answer with a number:

- [ ] Server topology chosen, and why.
- [ ] Players per area and target CCU.
- [ ] Vertical or horizontal progression, and who feeds the content.
- [ ] Why strangers cooperate (at least one mechanism).
- [ ] Which systems need critical mass, and the minimum count for each.
- [ ] What a player does after 300 hours.
- [ ] Content production rate versus consumption rate.
- [ ] What the server decides, and where the bot incentives are.
- [ ] TTFF in minutes.
- [ ] Whether the game works with 20 players online.
- [ ] Revenue model, and what it does to the design.
