# 4X and grand strategy

Read when the player directs an empire through exploration, expansion, exploitation and conflict. Put the turn loop in file 02, map rules in file 03, research in file 04, resource flows in file 06 and victory rules in the file that owns the campaign loop. Link to those owners rather than duplicating rules.

All balancing values below are illustrative examples for an invented game, not shipped-game data or recommended defaults. Every section records the chosen rule, its reason, a rejected alternative and a measurable target. For real-time grand strategy, define a simulation period and express the same budgets per day or month instead of per turn.

## Campaigns are measured in decisions and turns

Choose a target campaign duration before choosing the map size. Separate player decision time, animation time and simulation wait. Increasing the turn limit changes all three costs.

```text
campaign minutes = turns × (decision seconds + animation seconds + wait seconds) / 60
```

Example: 120 turns at an average of 75 decision seconds, 10 animation seconds and 5 wait seconds take 180 minutes. Record early, middle and late-game budgets separately; a single average can hide an hour of repetitive orders at the end.

Example decision: a 3-hour campaign with a turn-120 score finish supports a complete evening session. Reject an unlimited conquest-only finish if players are expected to complete campaigns regularly. Decide whether pausing, saving and simultaneous turns change the intended session length.

## Map density decides contact and conquest time

Measure useful space, not just total tiles. Record traversable land, settlement sites, travel costs, chokepoints and start spacing. Link terrain and traversal assumptions to [world.md](world.md).

For a simplified land route:

```text
travel turns = ceil(route movement cost / movement points per turn)
```

Example: a 24-tile route costing 1 movement point per tile takes 12 turns at 2 movement points per turn. On a 120-turn map, that trip consumes 10% of the campaign before combat. Roads, transports and hostile borders must have explicit effects on that budget.

| Example map variable | Choice | Reason and rejected alternative |
|---|---|---|
| Playable area | 600 traversable land tiles for 6 factions | 100 tiles per faction is a starting density budget; reject counting inaccessible ocean as expansion space |
| Settlement sites | 30, distributed with comparable starting access | Roughly 5 per faction before conquest; reject unrestricted settlement if city count drives tedious orders |
| First contact | Target turns 8 to 12 in generated starts | Leaves an opening to explore; reject neighbours visible immediately if discovery matters |
| Cross-map expedition | At most 20 turns after transport unlocks | Keeps a distant victory threat contestable; reject routes longer than the response window |

These are generator acceptance targets, not guarantees from map dimensions. Test actual paths across many seeds. Record an allowed failure rate and how invalid starts are repaired or rejected.

## Resources come in jobs and opportunity costs

Choose what each resource prevents the player from doing simultaneously. If every resource purchases the same actions at a fixed exchange rate, explain why they are separate.

Example turn economy:

| Resource | Example income | Example use | Decision it creates |
|---|---:|---|---|
| Food | 12 per turn | 8 upkeep plus growth reserve | Expand population or tolerate a smaller settlement |
| Production | 10 per turn | A workshop costs 60; a unit costs 40 | Build future capacity or immediate defence |
| Research | 8 per turn | A technology costs 80 | Choose which capability arrives in 10 turns |
| Treasury | 15 per turn | 9 upkeep plus purchases | Maintain forces or save for an emergency |

Define stockpiles, caps, conversion, overflow, rounding and resolution order. Example: collect income, pay upkeep, then apply production; unused production carries over only within the same queue. Reject silent overflow loss if players are supposed to plan exact completion turns.

A 60-production workshop that adds 3 production per turn has a simple payback time of 20 operating turns after completion, excluding upkeep and lost alternatives. Building it at 10 production per turn takes 6 turns first. Compare that 26-turn horizon with the remaining campaign and the value of the unit delayed.

Use [economy.md](economy.md) for source and sink accounting. Keep per-turn rates distinct from stockpiles and one-time rewards. Document shortages: which unit, building or population is affected first, and whether the player chooses.

## Expansion rules shape the snowball

Measure the feedback loop: territory adds output, output buys conquest, conquest adds territory. Choose where this loop has a cost, a delay or a counterplay opportunity. Reject hidden penalties that reverse success without a readable rule.

| Control | Example rule | Reason | Alternative rejected |
|---|---|---|---|
| Administration | Each city beyond the first 4 costs 3 treasury per turn | Expansion competes with military upkeep | A hard city cap prevents emergency conquest |
| Integration | A captured city supplies half output for 8 turns | Creates time for a counterattack | Immediate full output rewards uninterrupted conquest too quickly |
| Logistics | Units beyond supply range consume 2 extra treasury per turn | Distant wars require preparation | Global damage penalties are hard to connect to geography |
| Diplomacy | Show a threat score and the threshold for defensive pacts | Rivals can coordinate against expansion | Unannounced automatic wars remove negotiation |

Specify thresholds, stacking and who sees the rule. Example integration uses fractional internal output and rounds only when displaying it; reject repeated integer rounding if it makes low-output cities contribute nothing.

Test both the leader and the recovering player. Example acceptance target: at turn 60, a 20% production lead should not make victory inevitable under competent opposing play. Record how many seeded matches and which policies were tested. Do not claim a comeback is possible merely because the interface still permits orders.

## Victory conditions gate the end of the campaign

Choose whether victory rewards a single dominant strategy or several commitments with different counters. The [official Civilization VI manual](https://downloads.2kgames.com/civilization/vi/manuals/eu/CIV_VI_25TH_ONLINE_MANUAL_ENG.pdf) provides a shipped comparison with multiple victory paths. The invented conditions below are design examples, not that game's rules.

| Example path | Exact finish condition | Warning and counterplay | Why not require conquest? |
|---|---|---|---|
| Territorial | Hold 4 of 6 marked capitals for 5 consecutive turns | Public countdown; recapture any one to reset it | Requires a contestable objective rather than eliminating every unit |
| Research | Complete 3 linked projects, each costing 100 research | Public project milestones; interrupt the required facility | Gives a compact empire a route to win |
| Federation | Gain 4 faction votes at a council after turn 80 | Publish commitments 5 turns ahead; diplomacy can change votes | Makes relationships an objective rather than a temporary combat bonus |
| Score | Highest declared score at turn 120 | Show the scoring formula throughout the game | Bounds duration when no specialised path completes |

Record tie-breaking, simultaneous victories, eliminated factions, abstentions and allied wins. Example: evaluate at the end of a full round, then use score and a declared secondary metric to break a tie. Reject player-order priority if simultaneous-turn fairness matters.

Calculate the response window against travel and production time. A 5-turn warning cannot be answered by a force 12 turns away without another counter. Either extend the warning, provide a remote response or intentionally make earlier intelligence necessary.

## How the team scopes the late game

Choose the maximum useful management burden before adding more cities or unit types. Example: 12 cities with 3 routine orders each at 4 seconds per order cost 144 seconds every turn, before strategic decisions. This already exceeds the earlier 75-second average decision budget.

Record which routine actions can be queued, delegated or resolved in bulk. Example choice: city production queues and a priority list handle routine replacements, while border changes require explicit confirmation. Reject automatic strategic purchases if spending reserves is meant to remain a player decision.

Set a late-game target, such as no more than 30 seconds of routine orders per turn in a 12-city test save. Measure it with the proposed interface rather than assuming automation solves the problem. Expose what automation did and let players override its policy.

Example vertical slice: 2 factions, 8 settlement sites, 3 resources, 2 victory paths and a 30-turn scenario. Budget AI policies, save-state testing and end-turn performance in file 12. Reject a larger map until the slice produces competing plans and a timely finish.

## Traps to warn about in the document

- Map size grows without a movement or turn-count change. Recalculate contact and response times.
- More territory grants only benefits. Compare marginal income with administration, defence and integration costs.
- Every victory uses the same production race. Give each commitment a different counter and opportunity cost.
- The winner is known long before the game ends. Measure turns between a decisive lead and formal victory; test surrender or an accelerated ending.
- Automation hides important decisions. Separate routine execution from irreversible strategic choices.
- AI speed measured only in an opening save misses the costly state. Benchmark the maximum supported late-game map and unit count.

For each trap, record a threshold, the chosen remedy and a rejected alternative. Example: if the median finish takes more than 20 turns after a decisive lead, shorten the objective hold period before increasing every unit's movement.

## The strategy design is done when

- [ ] Campaign turns, session time and early-to-late decision budgets agree.
- [ ] Map size, usable space, start spacing, contact and cross-map travel are quantified.
- [ ] Resource rates, stockpiles, upkeep, queues, overflow and resolution order are explicit.
- [ ] Expansion has readable costs and measured counterplay windows.
- [ ] Each victory path has exact conditions, warnings, counters and tie rules.
- [ ] A distant player can respond within the intended victory window.
- [ ] Routine late-game orders have a measured time budget and delegation policy.
- [ ] The slice budgets content, AI, save-state tests and end-turn performance.
- [ ] Each section records rejected alternatives and marks unresolved choices with `[UNDECIDED: ...]`.
