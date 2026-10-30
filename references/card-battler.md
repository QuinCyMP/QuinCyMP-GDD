# Card battlers and deckbuilders

Read when cards define the player's combat choices. Put the encounter loop in file 02, collection and unlock rules in file 04, card resolution in file 05 and acquisition costs in file 06. Use this reference for constructed decks, draft formats and decks assembled during a run; choose which model applies before borrowing its numbers.

All balance values below are illustrative examples for an invented game, not shipped-game data or recommended defaults. Record what was chosen, why, a rejected alternative and a measurable target in every section.

## Decks are measured in access to decisions

Decide deck size together with opening hand, draw rate, copy limit, mulligan and reshuffle rules. A card that exists in the collection but rarely appears in play does not reliably define an archetype.

Example rules: exactly 20 cards, at most 2 copies of a card, a 5-card opening hand, 1 draw per turn after the first and no mulligan. Hands persist between turns. Played cards enter a discard pile; reshuffle it only when the draw pile is empty. Reject full-hand redraws if preserving a setup across turns is the intended skill.

For a shuffled deck drawn without replacement:

```text
P(at least one desired card) = 1 - C(N - K, H) / C(N, H)
N = deck size; K = desired copies; H = cards drawn; C = combinations
```

With the example 20-card deck, 2 desired copies and 5 opening draws, the probability is about 44.7%. By 8 draws it is about 65.3%. This calculation excludes mulligans, search, extra draw and reshuffling. Specify those rules before using the result to claim consistency.

Choose a target turn for a build's first meaningful decision. Example: a setup deck should find a useful enabler by turn 4 in at least 80% of simulated games. Reject increasing every card's damage when the actual problem is access to enablers.

## The energy curve decides playable density

Choose resource supply and card cost distribution together. Fixed energy, growing mana and resources drawn as cards create different failure states.

| Resource model | Choice it creates | Risk to measure | Example test target |
|---|---|---|---|
| Fixed energy refreshed each turn | Spend now or hold a card for a later combination | Too many unplayable expensive cards | No playable card in fewer than 5% of ordinary hands |
| Mana capacity grows each turn | Plan an early, middle and late curve | Early hands dominated by late cards | At least 1 affordable play on each of the first 3 turns in 90% of games |
| Resource cards in the deck | Trade action density for resource reliability | Too few or too many resources | Report both failure rates separately over 1,000 seeded draws |

Example choice: 3 energy refreshed every turn, no banking, and costs of 0, 1, 2 and 3 distributed across 2, 8, 6 and 4 cards. The 20-card deck has an average cost of 1.6. Reject accumulating unused energy if the desired decision is which cards to combine this turn.

Average cost alone is insufficient. Count affordable combinations in actual hands, unused energy, card draw and the share of hands containing only conditional actions. A zero-cost card that replaces itself also changes access to every other card.

## Cards and rewards come in roles

Keep one authoritative card table with ID, cost, targeting, effect, conditions, rarity, archetype, copy limit and upgrade. State resolution order for simultaneous effects. Use invented names when drafting examples.

Example rarity distribution for a 60-card library:

| Rarity | Distinct cards | Probability for each reward slot | Intended role |
|---|---:|---:|---|
| Common | 36 | 70% | Enablers and dependable baseline actions |
| Uncommon | 18 | 25% | Specialised payoffs and flexible answers |
| Rare | 6 | 5% | Build-changing effects with a real limitation |

These are two different distributions: card counts and offer probabilities. Define the sampler. Example: each of 3 reward slots independently rolls rarity, then draws uniformly from that rarity, with duplicates allowed. The chance of at least one rare offer is `1 - 0.95^3`, about 14.3%, not 15%.

If duplicate offers are rejected, rarity is guaranteed or pity exists, specify the replacement algorithm and recompute probabilities. Link to [economy.md](economy.md) for pity and drop-rate reasoning. Reject mandatory rare enablers if an archetype is meant to be available reliably.

Decide whether players may skip a reward, remove a card or replace one at the deck limit. Example: replacing a card keeps a 20-card deck constant and preserves access probabilities. Reject forced additions if rewards are supposed to improve a carefully tuned deck.

## Archetypes shape the available actions

Follow the boundary method in [classes-and-skills.md](classes-and-skills.md): define what each build can do, what it cannot do and which other build owns that function. Different artwork and damage types do not establish a boundary.

| Example archetype | Its exclusive hook | Boundary | Example numeric test |
|---|---|---|---|
| Cinder ledger | Save charges from actions to spend on a later burst | Cannot heal; holding charges sacrifices immediate damage | Burst requires at least 2 setup turns |
| Glass bastion | Convert unspent defence into a next-turn attack | Cannot retain defence indefinitely | Conversion consumes all stored defence after 1 turn |
| Thread engine | Reorder upcoming draws to assemble combinations | Cannot generate energy | At most 2 cards reordered per action |

Reject giving all three builds efficient draw, healing and burst merely to equalise win rate. Change costs or encounter matchups while preserving their weaknesses. Record the reason for every shared utility card and the maximum copies permitted.

Example matchup target: no supported starter matchup below a 40% win rate under a stated pilot policy. This is a playtest goal, not a claim of balance. Measure first-player advantage, pilot experience and encounter distribution separately before changing an archetype.

## Collection growth and deck limits are separate gates

Use the library-versus-slots distinction from [classes-and-skills.md](classes-and-skills.md). The legal card library is what the player can choose from. The deck is what they bring. The hand and energy supply limit what they can use now.

Example collection plan:

| Milestone | Legal distinct cards | Deck size | Maximum copies of one card | Intended decision |
|---|---:|---:|---:|---|
| Introduction | 24 | 20 | 2 | Replace a few obvious starter weaknesses |
| First mastery unlock | 40 | 20 | 2 | Choose between incompatible payoffs |
| Complete release pool | 60 | 20 | 2 | Build around different enablers and counters |

Keep deck size fixed in this example to make library growth add choices rather than dilute draws. Reject increasing the deck limit with every unlock unless longer, less consistent games are a deliberate goal. Record whether copies are owned separately and whether all unlocked cards are legal in every mode.

For a run-based deckbuilder, distinguish the global reward pool from cards acquired in the current run. Decide what unlocks permanently and what resets. [Mega Crit's Slay the Spire description](https://www.megacrit.com/press-kits/slay-the-spire/) presents building a deck from cards encountered while climbing. It is a useful comparison for choosing in-run acquisition instead of a fully constructed starting deck; it does not supply the example counts above.

## How the team scopes a testable card pool

Example slice: 24 cards, 2 archetypes, 3 enemy patterns and 1 reward path. Record the animation, text, implementation and test cost per new effect in file 12. Reject a large pool of nearly identical cards if the slice has not demonstrated distinct decisions.

Count interactions as well as cards. Twenty-four distinct cards produce 276 unordered distinct pairs before considering duplicates, sequences or enemy effects. Prioritise interactions involving copying, discounts, recursion, extra turns and draw loops.

Choose a numeric stop rule for automated resolution. Example: stop a test after 1,000 effects without a player decision and report the action trace. This diagnoses a loop; it is not a shipped rule for resolving one. Decide separately whether the design prevents, caps or intentionally supports repeatable combinations.

## Traps to warn about in the document

- A rarity label used as a power multiplier makes common cards obsolete. Compare cost-adjusted utility and preserve enablers at accessible rarities.
- Library size mistaken for deck size hides loss of consistency. Recompute draw probabilities after every deck-size change.
- More draw used to fix every weak archetype erases the distinction between builds. Specify who owns draw manipulation.
- Forced rewards can make a winning deck worse. State skip, removal and replacement policies.
- Aggregate win rate can hide unplayable matchups. Report matchup and first-player results with sample counts.

For each trap, write the failure threshold and rejected remedy. Example: if a starter fails to make any legal play in more than 5% of opening hands, change its curve before adding a universal free redraw.

## The card design is done when

- [ ] Deck limits, copies, hand size, drawing, mulligan, discard and reshuffle rules are explicit.
- [ ] Access to key actions is calculated under those rules.
- [ ] Resource supply, cost distribution and unplayable-hand targets agree.
- [ ] The card table owns costs, effects, targeting and resolution rules.
- [ ] Rarity counts, reward probabilities and duplicate handling are separate and complete.
- [ ] Archetypes have exclusive hooks, weaknesses and matchup tests.
- [ ] Library growth, deck limits and run resets are distinct decisions.
- [ ] The slice has a content count and an interaction-testing budget.
- [ ] Each section records rejected alternatives and marks unresolved choices with `[UNDECIDED: ...]`.
