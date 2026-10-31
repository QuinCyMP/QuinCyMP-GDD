# Roguelikes and roguelites

Read when a game is organised around repeated runs. Put the run loop in file 02, the route in file 03, progression in file 04, failure in file 05 and seed or save requirements in file 11. Link between those owners instead of repeating rules.

Choose the run contract before debating the genre label: what starts a run, what ends it, what resets and what carries forward. Record each decision, its reason, rejected alternatives and the numbers needed to test it. Numerical claims about shipped games below have sources; project targets stay `[UNDECIDED: ...]` until chosen and measured.

## Runs are measured in time and decisions

Specify the target run length for a beginner, a returning player and a player who knows the route. Separate a successful run from an early failure. A completion-time average hides how much play happens before someone learns the game.

Budget the whole loop:

```text
run time = preparation + traversal + encounters + reward decisions + ending
retry time = death feedback + persistent progression choices + return to control
```

Decide whether a run must fit inside a session. If not, specify suspend and resume behaviour. Reject forced uninterrupted play if the target player needs short sessions; reject unrestricted rewind if accepting consequences is the intended challenge.

| Required number | Why the document needs it | Unresolved target |
|---|---|---|
| Successful run duration | Sets the content and endurance budget | [UNDECIDED: target minutes by experience group] |
| Time to first meaningful choice | Determines how much opening content repeats without a decision | [UNDECIDED: seconds from starting a run] |
| Encounter and recovery time | Connects combat pacing to the complete run | [UNDECIDED: duration distribution and recovery budget] |
| Death-to-retry time | Measures the friction of learning from failure | [UNDECIDED: maximum time until control returns] |

Record whether menus, pauses and story scenes count in these measurements. Compare proposed targets with the intended session budget rather than copying another game's duration.

## Encounter density decides run structure

Work backward from the time budget to the route. Choose fixed stages, branching nodes, free exploration or a hybrid. Record where the player can trade safety for rewards and what information is available before that choice.

```text
encounter budget = run-time budget - non-encounter time
encounter count estimate = encounter budget / typical encounter duration
```

This is a planning estimate, not a substitute for measuring complete runs. Reward deliberation, backtracking and boss retries can change the result. Record the distribution as well as the average.

| Route choice | What the player decides | Alternative to reject with a reason | Numbers to choose |
|---|---|---|---|
| Fixed sequence | How to survive known constraints with a changing build | Branching paths if route planning adds no useful decision | Stages, encounters and recovery opportunities |
| Branching map | Which risk and reward to accept next | Hidden routes if the choice needs informed planning | Branches, visible future nodes and mandatory fights |
| Explorable area | When to leave, and whether to revisit | A fixed corridor if navigation is the main skill | Travel time, optional sites and backtracking budget |

For a shipped comparison, [Mega Crit's Slay the Spire press kit](https://www.megacrit.com/press-kits/slay-the-spire/) lists procedurally generated levels. This supports studying generation as a route choice; it does not establish an ideal run length or encounter density.

## Encounters and rewards come in roles

Define what each encounter tests before writing a large pool. Choose pressure, recovery, build commitment and information as distinct jobs. Record the frequency and placement constraints that keep a route playable.

| Role | Decision it should create | Failure to test | Required numbers |
|---|---|---|---|
| Ordinary encounter | Spend a resource now or preserve it | Every fight rewards the same action | Expected damage, duration and reward |
| Optional danger | Risk the run to strengthen a build | Reward is mandatory for survival later | Success rate and expected reward by build |
| Recovery | Trade immediate safety against future power | Recovery makes all earlier losses irrelevant | Healing cap, cost and spacing |
| Build reward | Commit, pivot or decline | Random offers repeatedly lack usable choices | Offer count, pool weights and reroll limits |
| Boss or gate | Demonstrate mastery of the current stage | A valid build has no possible answer | Damage budget, phase duration and counter coverage |

Use [classes-and-skills.md](classes-and-skills.md) for build boundaries and [economy.md](economy.md) for reward probabilities. Keep the authoritative probabilities in data tables. Reject a reward system that requires an unavailable rare effect unless an alternate route is explicitly part of the design.

Content counts are project-specific. [Mega Crit's press kit](https://www.megacrit.com/press-kits/slay-the-spire/) lists four core characters, more than 300 cards and more than 50 combat encounters for Slay the Spire. Those are published content counts, not a minimum production target or proof that a smaller pool cannot support replay.

## Seeds and player actions shape the run

Choose what a seed promises: the starting map, the reward stream, a complete replay under identical inputs, or only a shareable challenge identifier. These promises are different. Do not call the whole game deterministic because its map generator accepts a seed.

Record these decisions in file 11:

| Decision | Why it matters | Rejected alternative to discuss | Numbers to specify |
|---|---|---|---|
| Random streams | Separate map and cosmetic randomness can keep unrelated changes from changing routes | A shared stream if an animation changes the next reward | Seed width and saved generator-state size |
| Replay inputs | A seed alone omits player choices and timing | Seed-only bug reports when input order changes results | Input precision, log size and retention limit |
| Version compatibility | Content and algorithm changes can alter a seeded run | An indefinite cross-version promise without a compatibility plan | Supported version range and migration budget |
| Save boundaries | A resumed run needs the same relevant state | Saving only the seed when inventory and random state have advanced | Save frequency and maximum lost play time |

Verify repeated generation, save/resume and a replay with the same inputs. Compare route, rewards and combat outcomes separately. Include build version, modifiers and unlock state in a reproduction record. Reject silent reseeding on load if the design promises the same future outcomes after resuming.

## Progression and death gate the next attempt

Separate player knowledge, within-run power and persistent progression. Each needs a purpose. Permanent options can widen builds; permanent power can help a struggling player; neither should be added without deciding how it changes difficulty.

| Layer | What may persist | What must be decided | Required numbers |
|---|---|---|---|
| Player knowledge | Enemy patterns and route understanding | Which failures teach a visible lesson | Attempts to demonstrate the intended skill |
| Within-run progression | Usually resets at the run boundary | Which items, upgrades and resources disappear | Power curve and acquisition rate during a run |
| Persistent options | Characters, equipment choices or reward-pool entries | Whether unlocking an option dilutes future offers | Library size, equipped slots and unlock pacing |
| Persistent power | Starting resilience or resource advantages | Whether repeated failure buys eventual success | Beginner-to-veteran power ratio and maximum bonus |
| Story state | Relationships, discoveries and dialogue | What failure advances without requiring victory | Events per return and repeat frequency |

[Supergiant's Hades FAQ](https://www.supergiantgames.com/blog/hades-faq/) describes carrying knowledge into randomized runs, permanent progression and difficulty modifiers. It also describes God Mode becoming more protective after deaths. These are design alternatives to inspect, not evidence for a universal power curve or required number of failed attempts.

Specify death, victory, abandonment, disconnect and save deletion separately. Write a reset ledger listing every resource and flag, its owner and whether it survives each ending. Reject treating abandonment as death if doing so creates a profitable reward exploit; reject a different penalty if it punishes a legitimate interruption.

Difficulty scaling must name the affected behaviour. Choose enemy patterns, resource scarcity, time pressure or numerical power changes, then state the increments and cap. Record which modifiers stack, how rewards change and whether assistance affects progression. Reject health-only scaling if it lengthens runs without demanding a new decision.

Measure success and failure by experience, unlock state and chosen modifiers. Keep assisted and unassisted results distinguishable. Decide the next-attempt goal after an early death, a late death and a victory; repeating the same opening should have a reason.

## How the team scopes repeatable content

Choose a slice that contains a complete run, a failure and a meaningful next attempt. List the encounter roles, reward combinations, route variants and persistent choices it must prove. Put their counts, production estimates and test budget in file 12.

Reject expanding the pool before the slice demonstrates that different builds produce different decisions. Test combinations that change resource costs, repeat effects, skip encounters or alter reward selection. A pool's entry count does not describe its interaction cost.

Record `[UNDECIDED: content counts, production budget and acceptance criteria for the slice]` until the team can cost the chosen scope. State what is cut and the evidence that would justify restoring it.

## Traps to warn about in the document

- Repetition is mistaken for replayability. Measure how soon attempts diverge and explain the decisions causing that divergence.
- Permanent power disguises an unreadable encounter. Compare failure causes before and after upgrades, rather than only comparing win rates.
- Randomness removes every answer to a required threat. Record generator constraints and alternative solutions, then test generated routes against them.
- Unlocks dilute the reward pool. Recompute access to build enablers as the library grows.
- A retry preserves rewards without preserving the intended cost. Check the reset ledger against each ending and reload path.
- Save/resume changes seeded outcomes. Test the precise replay promise instead of assuming a matching seed proves it.

For each trap, choose a numerical failure threshold and a remedy. Record why the alternative remedy was rejected. Leave an explicit question marker when no evidence supports the threshold yet.

## The roguelike design is done when

- [ ] Run start, victory, failure and abandonment have explicit rules.
- [ ] Run duration and retry time have targets for the intended player groups.
- [ ] Route structure, encounter roles and recovery opportunities fit that budget.
- [ ] Within-run progress, persistent options, persistent power and knowledge are separate.
- [ ] A reset ledger covers every resource and ending.
- [ ] Seed, replay, save/resume and version promises have reproducible checks.
- [ ] Difficulty increments, caps, assistance and reward effects are specified.
- [ ] The slice has content counts, a production budget and acceptance criteria.
- [ ] Every section records rejected alternatives and marks missing decisions honestly.
- [ ] Every numerical claim about a shipped game has a source; project targets are identified as decisions rather than borrowed benchmarks.
