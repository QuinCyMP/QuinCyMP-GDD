# Open world

Read when writing `03-world.md`, or when the user talks about world size, maps, exploration or travel.

## Worlds are measured in time and density, not km²

Players never feel "how many square kilometres". They feel **travel time** and **how often something interesting appears on the way**. A dense 4 km² world feels larger than an empty 40 km² world every time, and that is the advantage a small team must use.

Three numbers always in the document:

```
1. world size         (km²)
2. travel speed       (m/s per travel mode)
3. time to cross      = distance ÷ speed
```

Written correctly:

> World 6 km² (2.45 × 2.45 km) · on foot 4.5 m/s · mounted 9 m/s.
> Crossing takes 9 minutes on foot, 4.5 minutes mounted.
> This size was chosen because trips over 10 minutes stop players exploring, and because one person can hand-build about 40 landmarks in 8 months.

## Density decides the size

```
points of interest needed = time to cross (seconds) ÷ target spacing (seconds)
```

Spacing by the feel wanted:

| Spacing | Feel | Fits |
|---|---|---|
| 20 to 40 s | Dense, always something to do | Combat-focused games where players want no idle time |
| 40 to 90 s | Balanced, room to breathe | The safest default |
| 2 to 5 min | Lonely and wide, travel is content | Atmosphere, risk, survival |
| 5 min and up | Empty | Nearly always a mistake, not a design |

Run the rule backwards (the small-team move): start from the number of landmarks the team can build, multiply by the spacing wanted, get the crossing time, get the world size. Never start from the size wanted; it always yields an empty world.

## Points of interest come in kinds

Count density across kinds with different costs. Do not count only dungeons.

| Kind | Production cost | Suggested share |
|---|---|---|
| **Hand-built landmarks**: towns, ruins, dungeons | Very high | 10 to 15% |
| **Placed encounters**: mob groups, camps, other players | Low, reuses assets | 30 to 40% |
| **Resources**: ore, herbs, fishing spots | Very low | 20 to 30% |
| **Vistas and terrain** | Low, good terrain is free | 15 to 20% |
| **Secrets and environmental storytelling** | Low cost, very high return | 10 to 15% |

The last kind is the cheapest thing that feels the most expensive. An adventurer's corpse beside a chest that will not open tells a story with no scripting at all. A small team invests here heavily.

## Traversal shapes the world

Choose the **travel verbs** before laying out the map. Each verb reshapes the world:

| Verb | The world must be | Side effect |
|---|---|---|
| Walk and run only | Small and dense | Travel is boring if the world is large |
| Mounts and vehicles | Can be wide, needs roads | Players skip the content in between |
| Climbing | Vertical terrain means something | Breaks gating by walls |
| Gliding, flying | Designed from above as well | Kills nearly all ground encounters |
| Fast travel | Removes the pain | Shrinks the felt size; needs a cost attached |

The document answers: is there fast travel, how is it unlocked, what does it cost. The answer changes the economy and the politics of the whole game. A world with free travel has no territory worth holding.

## Zoning and gating

Three methods, more than one allowed:

- **Level gate.** Mobs too strong. Straightforward, feels like an artificial wall.
- **Skill gate.** An ability is required (swim, climb, heat resistance). Feels natural.
- **Knowledge gate.** You have to know the way. Cheapest, most powerful, and what a small team should use most, because it builds nothing and still creates real discovery. It also makes **information valuable in an MMO**: veterans teaching newcomers is social interaction that appears on its own.

## How a small team builds a big world

By value:

1. **A small, dense world.** The most direct answer and nearly always the right one. 2 to 8 km² where every square metre is intentional beats 50 km² where 90% is empty field.
2. **A modular kit.** 30 to 50 pieces assembled into unlimited buildings and ruins. Fixed cost, unlimited output. Write it as a requirement in `10-art-audio.md`.
3. **Procedural terrain plus hand-built landmarks.** Tools make the terrain and filler; the landmarks are made by hand, and landmarks are all players remember anyway.
4. **A world players change.** Let them build, destroy and own, so the world keeps changing without the team producing more. The mechanism that most makes a small-team MMO possible.
5. **Seasons and cycles.** The same area changes state on a cycle: content × N from one asset set.

## Traps to warn about in the document

- **Too large a world kills the MMO.** When players spread until they never meet, the game feels like single-player with lag. Compute `online players ÷ world size`; below **5 players per km²** on a weekday, the world is too big.
- **Sculpting terrain before the traversal verb is chosen.** It will be redone.
- **Wide world and deep content at once.** A small team gets one. Write down which.
- **Ignoring streaming at design time.** A seamless world and a zoned world differ in architecture, not decoration. Record it in `11-tech-assumptions.md`.

## File 03 is done when

- [ ] World size is a number, with a reason tied to the team's production capacity.
- [ ] Every travel speed and the time to cross.
- [ ] Target spacing of points of interest, and their count per kind.
- [ ] The traversal verbs chosen and their effect on the world's shape.
- [ ] Fast travel, yes or no, and its cost.
- [ ] The gating methods used.
- [ ] Player density per km² on a weekday.
- [ ] Which of the five building strategies above this team uses.
- [ ] Alternatives considered and rejected, with reasons.
