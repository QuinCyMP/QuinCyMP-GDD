# Survival and crafting

Read when the core loop is gathering, crafting, surviving and building a base. Put the loop in file 02, the resource geography in file 03, progression in file 04, death in file 05, material flows in file 06 and raid rules in file 07. Link to each rule's owner rather than copying it.

All balancing numbers below are illustrative examples for an invented game, not shipped-game data or recommended defaults. For every decision, record the reason, a rejected alternative and the number that will prove the choice works.

## Survival is measured in time to danger

Choose whether needs threaten death, reduce capability or reward preparation. This decides whether a trip is a deadline or an opportunity to improve its outcome. Reject a lethal hunger meter if the intended experience lets players build without interruption.

[Valheim's official FAQ](https://www.valheimgame.com/faq/) describes food as affecting health and stamina without being required to stay alive. Use that as an alternative to starvation, not as a source for the example rates below.

| Need | Example tick rule | Example consequence | Decision to record |
|---|---|---|---|
| Hunger | Starts at 100; loses 1 point every 30 seconds while active | At 0, lose 1 health every 10 seconds | Does food refill a meter or grant a temporary benefit? |
| Thirst | Starts at 100; loses 1 point every 20 seconds while active | Below 20, stamina recovery is halved | Does sprinting increase consumption, and by how much? |
| Cold exposure | Starts at 0; gains 2 points every 10 seconds below 0°C without insulation | At 60, lose 2 health every 10 seconds | Which clothing, shelter and weather combinations stop exposure? |

For constant depletion:

```text
time to empty = current points / points lost per tick × tick interval
```

The example hunger meter lasts 50 minutes from full. Thirst lasts 33 minutes 20 seconds. Cold exposure reaches its damage threshold after 5 minutes. These are separate clocks; do not use one generic survival timer.

State when ticks run: paused menus, sleep, disconnected characters and empty servers. Example choice: freeze personal needs while disconnected to support irregular co-op sessions. Reject offline starvation; quantify the remaining world simulation separately.

## Resource density decides the expedition

Work backward from the forage-to-fortify loop:

```text
prepare supplies -> travel -> gather -> return -> craft -> fortify -> reach a riskier resource
```

Example session budget: 3 minutes preparing, 4 travelling out, 8 gathering, 4 returning and 6 crafting or building equals 25 minutes. It fits inside the example full thirst meter, but starts with little reserve if the player departs partly depleted. Record required supplies and a failed-trip recovery budget.

Choose deposit spacing from travel and gathering time using [world.md](world.md). Record node yield, depletion, respawn, carrying weight and the number of players sharing a deposit. Reject instant respawns beside the base if expeditions are supposed to matter.

A useful comparison is useful materials delivered per minute, including the return journey. Example: 24 units over 12 minutes gives 2 units per minute; a distant 40-unit deposit over 25 minutes gives only 1.6. The distant deposit needs another benefit or a transport upgrade.

## Materials come in roles

Keep the authoritative recipes and material rows in `data/`, linked from file 06. Use [economy.md](economy.md) for sources and sinks. State quantities and units rather than calling a material common or scarce.

Example material table:

| Material | Source and yield | Weight per unit | Recipe or sink | Reason for its role |
|---|---|---|---|---|
| Reedwood | 6 per grove; 10-minute respawn | 1 kg | 8 per wall; 2 per repair | Renewable bulk supports repeated construction |
| Ash cord | 4 per fibre patch; 8-minute respawn | 0.25 kg | 2 per wall; 1 per tool repair | Shared demand makes building compete with upkeep |
| Ember ore | 3 per exposed vein; no respawn | 2 kg | 6 per furnace upgrade | Finite deposits pull expeditions outward |

Example wall recipe: 8 Reedwood + 2 Ash cord, 30 seconds at a bench, 1 wall output. Record salvage explicitly: dismantling returns 4 Reedwood + 1 Ash cord. Reject full salvage if relocation is meant to consume resources; reject no salvage if experimentation should be cheap.

Specify whether recipes consume fuel, require tools and produce by-products. Calculate demand per base tier and per repair cycle. A material with no recurring sink will accumulate after construction ends.

## Building and raids shape the base

Choose the threat model before setting wall health. A shelter against weather, a defence against creatures and a fort against players need different rules.

| Decision | Example choice and reason | Alternative rejected and why |
|---|---|---|
| Placement | A 20-metre claim radius, with collision and access checks, makes ownership visible | Unrestricted overlap allows another player to block the entrance |
| Structural support | A piece may span 3 unsupported cells, making supports readable | Hidden load simulation makes failures difficult to predict |
| Damage | A wall has 600 health; a raider deals 20 damage each second | Universal damage from every tool makes early walls disposable |
| Raid eligibility | Creature raids require a base owner online; warn 60 seconds before arrival | Offline destruction punishes absence in this co-op design |
| Raid frequency | At most 1 raid per 30 active minutes; the timer pauses during raids | Independent random rolls can produce consecutive attacks |
| Permissions | Only invited builders may dismantle; visitors cannot open storage | Shared edit access lets a guest erase progression |

At the example damage rate, one unopposed raider breaks a wall in 30 seconds. Three raiders focusing it need 10 seconds. Compare both with the time a defender needs to arrive, not just with weapon damage.

For PvP, replace the example eligibility rule with explicit raid windows, attacker limits, safe zones and post-raid protection. State whether logging out cancels an active raid. Reject a logout escape if raids are intended to resolve after combat begins.

## Progression and death gate the next trip

Choose what opens each region: equipment, knowledge, a crafted station or a world event. Example: insulation stops cold accumulation in the next region, but does not increase combat damage. Reject a universal tier multiplier if each region should demand a different preparation choice.

Specify death as a recovery loop, not just a percentage penalty:

| Question | Example decision | Reason and rejected alternative |
|---|---|---|
| What is lost? | Carried materials drop; equipped tools remain | Allows retrieval without crafting the same tools again; reject total loss |
| Where is the player returned? | Last claimed shelter, with a fallback at the start | Preserves a reachable recovery route; reject spawning at the corpse |
| How long can recovery take? | Target 5 minutes; the cache persists for 30 active minutes | Creates a detour without erasing a session; reject permanent destruction on death |
| What if they die again? | Keep both caches until each expires | Prevents a second death deleting the first recovery target |

Record who can loot a cache, whether expiry pauses offline and what happens inside an inaccessible raid area. Test the return trip with starter supplies and no help. Reject a death penalty that consumes the equipment required to recover that equipment.

## How the team scopes a complete survival loop

Choose a slice that proves gathering changes the base and the base changes the next trip. Example scope: 1 biome, 3 materials, 1 tool upgrade, 4 building pieces and 1 raid type. Budget production and testing time in file 12.

Reject adding another biome before this slice demonstrates a reason to leave safety. Count recipe interactions, weather states and party sizes as test work. Record what is cut and the measurable condition for restoring it.

## Traps to warn about in the document

- Needs that all deplete at the same rate create repeated menu work. Measure interruptions per session and decide which need creates a distinct choice.
- Repairs that consume the entire expedition yield prevent progress. Compare net materials after food, fuel and repairs with the next upgrade cost.
- Walls balanced against one attacker collapse under a group. Test maximum supported attackers and repairers together.
- Offline rules stated only for hunger leave raid and crop behaviour ambiguous. Give each clock an explicit rule.
- A recovery cache is not recoverable if its route requires the lost tool. Test the route after removing that tool.

For each identified trap, record a numerical failure threshold, the chosen remedy and why the alternative was rejected. Example: if upkeep consumes more than half the delivered materials across 3 ordinary trips, reduce repair demand before increasing deposit density.

## The survival design is done when

- [ ] Hunger, thirst and temperature each have units, tick intervals, thresholds and offline rules.
- [ ] One forage-to-fortify session has a complete time and supply budget.
- [ ] Materials have yields, weights, recipes, sinks and respawn rules.
- [ ] Base placement, support, ownership, damage and repair rules are explicit.
- [ ] Raid eligibility, warning, frequency, disconnect behaviour and permissions are decided.
- [ ] Region gates and the benefit of each upgrade have measurable effects.
- [ ] Death loss, respawn, recovery time, cache ownership and repeated death are specified.
- [ ] The slice has a content count, production budget and acceptance test.
- [ ] Each section records rejected alternatives and marks unresolved choices with `[UNDECIDED: ...]`.
