# Gacha and mobile live service

Read when collection draws, rotating banners or recurring mobile sessions shape the game.
Put acquisition and prices in file 06, progression in file 04, daily play in file 02 and the release calendar in file 13.
Record decisions, reasons, rejected alternatives and testable numbers in those owners rather than copying rules between files.
All worked numbers below are invented examples, not shipped-game benchmarks or values to copy.

## Collection is measured in access and time

Choose what the player collects and why another item changes a decision.
A larger catalogue is not useful progression if every new release replaces the previous answer.
Decide whether the game sells expression, additional options or power, and state the resulting promise to non-paying players.

| Required number | Decision it supports | Unresolved target |
|---|---|---|
| Time to a functional starting roster | Whether the core loop works before a purchase | [UNDECIDED: hours and guaranteed starter options] |
| Earned draws per calendar period | Whether saving can reach an advertised goal | [UNDECIDED: guaranteed income, excluding one-time gifts] |
| Maximum draws to a selected reward | Whether the acquisition promise is bounded | [UNDECIDED: target guarantee and its reset rules] |
| Power gap from purchases or duplicates | Whether competition remains credible | [UNDECIDED: maximum gap by mode] |
| Time needed to use a new reward | Whether acquisition delivers playable content | [UNDECIDED: upgrade resources and play hours] |

Reject a random starting roster if it can leave the player unable to use the core loop.
Reject direct power sales in a mode whose promise is equal competitive access unless the promise or matchmaking changes explicitly.
Record both the ordinary acquisition path and the path for someone who never pays.

## Banner cadence sets the saving horizon

Choose the banner interval from the acquisition promise and content plan.
Specify opening and closing instants with a timezone, overlap, reruns and whether missed rewards remain obtainable.
Compare earned currency over the same interval with the cost of a chosen guarantee.
Do not include launch gifts in recurring income or count an uncertain event reward as guaranteed income.

| Calendar decision | Why it matters | Alternative to reject with a reason | Numbers to choose |
|---|---|---|---|
| New banners versus reruns | Returning players need an acquisition route | Permanent absence if collection completion is promised | Interval, duration and rerun window |
| Overlapping banners | Players may need to divide savings | Shared currency without visible competing goals | Concurrent offers and guaranteed income |
| Counter carryover | Savings and draw progress may outlive a banner | Silent resets that contradict the displayed promise | Counter lifetime and applicable banner families |
| Event and banner coupling | A reward may require time after acquisition | Closing the upgrade event before a late acquisition can use it | Upgrade window and available attempts |

Invented example: a banner lasts 21 days and costs 160 Tokens per draw.
A guaranteed recurring income of 60 Tokens per day provides 1,260 Tokens, enough for 7 draws with 140 Tokens left.
That does not fund an 80-draw guarantee during one banner.
The document must choose a longer saving horizon, a different guarantee, more income or a different acquisition promise.
Show that choice before describing the offer as accessible through ordinary play.

Record [UNDECIDED: banner calendar, recurring income and the intended saving horizon].
Reject a calendar chosen only to increase purchase frequency if the required content and player time do not fit it.

## Offers have different jobs and trust costs

Choose allowed products before balancing the shop around revenue.
The boundaries below are design recommendations; record the game's own contract and the evidence used to accept an exception.

| Product | What it may sell | Trust boundary | Number to record |
|---|---|---|---|
| Cosmetics | Appearance and expression | Do not hide gameplay advantages inside cosmetic descriptions | Price and any gameplay effect |
| Characters or equipment | Additional play options | Show acquisition rules and whether required content assumes ownership | Guarantee cost and viable non-paying alternatives |
| Convenience | Less repetition or easier management | Do not create avoidable friction solely to sell its removal | Time saved and baseline session burden |
| Subscription or pass | A defined bundle over a stated term | Explain expiry, missed claims and completion requirements | Price, claim window and required play time |
| Random rewards | A disclosed chance at specified items | Do not hide odds, change the pool silently or imply an absent guarantee | Rates, counter state and maximum cost if bounded |

Treat fake scarcity, misleading countdowns and undisclosed paid advantages as rejected designs.
State why each would break the promise made by this game rather than assuming a cosmetic-only shop guarantees trust.
Show the real-money purchase needed for an offer, including pack rounding and remaining currency, alongside the virtual price.

[Apple's App Review Guidelines, section 3.1.1](https://developer.apple.com/app-store/review/guidelines/#in-app-purchase), require odds disclosure before purchasing randomized virtual items.
That source supports the disclosure requirement, not a universal price or approval of every monetization design.
Assign an owner to check current platform requirements before release and after a shop change.

## Pity and guarantees shape acquisition

Use [Economy math: drop rate and time to obtain](economy.md#2-drop-rate-and-time-to-obtain) as the home of the fixed-rate formulas.
Apply those formulas only while attempts are independent and the probability is unchanged.
A soft-pity schedule changes the probability by counter state; a hard guarantee changes the final attempt.
Use a state table or probability calculation over those states instead of applying the fixed-rate mean to the whole system.

| State or transition | Decision the design must record | Failure to test |
|---|---|---|
| Base rate and eligible pool | Rates for each reward and any weighting within a rarity | Rarity odds mistaken for target-item odds |
| Soft-pity counter | Which attempt increases the rate and the full schedule | Off-by-one disagreement between display and server |
| Hard guarantee | What reward is guaranteed and on which attempt | A rarity guarantee described as a chosen-item guarantee |
| Featured guarantee | Whether losing a featured selection changes the next selection | A lost guarantee after a banner change |
| Success and duplicates | Which counters reset and what duplicates become | A duplicate consumes progress without the disclosed compensation |
| Banner switch and expiry | Which counters transfer, stay separate or expire | An undocumented reset or shared counter |

Invented example: top-rarity chance is 1% for the first 79 attempts, with a top-rarity guarantee on attempt 80.
Assume every top-rarity result resets this counter and there is no soft pity.
Using the linked fixed-rate probability model for the pre-guarantee attempts, about 54.8% obtain a top-rarity result before attempt 80.
The hard cap is 80 attempts; the uncapped fixed-rate mean is not the expected cost of this capped system.
At 160 Tokens per attempt, the maximum is 12,800 Tokens from a fresh counter.
If the first top-rarity result may miss the featured item but the next one guarantees it, the featured cap becomes 160 attempts or 25,600 Tokens.
That bound assumes the featured guarantee persists and no other reset intervenes.

Record [UNDECIDED: rate schedule, target guarantee, duplicate rules and carryover].
Reject an unbounded target chase when the advertised product promises a bounded acquisition cost.
Test zero progress, the attempt before each threshold, the threshold, a success, a duplicate and a banner transition.
For a multi-draw purchase, specify whether rewards are resolved sequentially and how each result affects the next counter.

## Dailies and stamina gate recurring play

Choose whether stamina limits rewards, progression or access to the activity itself.
Explain what remains playable at zero stamina and what a returning player can recover after an absence.
Reject blocking all meaningful play if the intended session can continue after the reward budget is exhausted.

| Required rule | Why it matters | Numbers to choose |
|---|---|---|
| Regeneration and cap | Determines how often an account reaches full | Units per minute and capacity |
| Activity cost | Converts the resource budget into actual play | Units per attempt and typical duration |
| Overflow and stored refills | Determines what is lost while away | Storage limit, expiry and conversion |
| Daily and weekly tasks | Defines the recurring obligation | Completion time and reset instant |
| Catch-up and missed claims | Sets the cost of an absence | Recoverable rewards and recovery window |
| Paid refills | May change progression and competition | Price, purchase cap and resulting power gap |

Invented example: 120 stamina capacity, 1 unit per 6 minutes and a 20-unit activity cost.
A full bar funds 6 activities, and an empty bar fills in 12 hours.
Regeneration supplies 240 units per day only if the player avoids losing regeneration at the cap.
Do not present those 240 units as what every player receives; simulate the intended login schedule and starting balance.
A player who checks in less often may lose regeneration, and the document must decide whether that is acceptable.

Record [UNDECIDED: ordinary daily minutes, missed-day policy and stamina-free activities].
Reject a mandatory streak if missing a day destroys progress the game's casual-session promise says is durable.
Measure meaningful decisions separately from collection clicks, loading and repeated claims.

## Scope the service with revenue definitions and capacity

Keep production head count, release cost and support capacity in the scope file.
Choose a release cadence the team can sustain, including localization, testing, rollback and customer support.
Reject adding another banner slot before there is capacity to deliver its content and maintain existing purchases.
Record [UNDECIDED: releases per period, production cost and support capacity] in that scope owner.

Define revenue metrics before comparing them with another game or planning content spend.
Use the same reporting period, population and revenue basis throughout a comparison.
The following is an explicit project convention for purchase revenue; label ad revenue separately if it is included elsewhere.

| Metric | Definition for this project convention | Required reference or target |
|---|---|---|
| ARPU | Purchase revenue in the period divided by active users in that period | [UNDECIDED: currency, reporting period, cohort and evidence-backed target] |
| ARPPU | The same purchase revenue divided by unique paying users in that period | [UNDECIDED: currency, reporting period, cohort and evidence-backed target] |
| Payer conversion | Unique paying users divided by active users in the same period | [UNDECIDED: acquisition mix and target] |

[Unity's revenue performance reference](https://docs.unity.com/en-us/iap/reporting/revenue-performance-reference) defines ARPPU using IAP revenue and paying users, and ARPDAU using daily revenue and daily active players.
It supplies metric definitions, not a benchmark for this game's audience or a substitute for a stated period.
Do not compare a monthly ARPU with a daily ARPDAU or mix gross bookings, net receipts, taxes and refunds without reconciliation.
When the denominator is zero, report the metric as unavailable rather than dividing by zero or inventing a value.

Invented example: 1,000 active users, 50 paying users and 500 units of purchase revenue in the same period yield ARPU 0.5, ARPPU 10 and payer conversion 5%.
This is an arithmetic check, not a market forecast.
Reject a revenue target copied from a different genre, region or acquisition channel without comparable cohort evidence.
Measure refunds, complaints, retention and non-paying progression alongside revenue so a higher average cannot hide a broken promise.

## Traps to warn about in the document

- A rarity guarantee is sold as a target guarantee. Name the exact reward set and calculate the target bound separately.
- Calendar income includes one-time gifts. Separate recurring, event-dependent and launch sources.
- A paid duplicate is assumed necessary for ordinary play. Test the advertised core loop with the guaranteed roster.
- Pity silently resets when a banner rotates. Publish and test transfer rules before taking payment.
- Stamina income assumes constant attendance. Simulate actual sessions and the cap.
- A daily task exists only to increase return frequency. State its gameplay decision and reject it if it has none.
- ARPPU rises because low-spending players leave. Inspect payer counts and retention before calling it success.
- A pass sells rewards that cannot be earned within the target player's available time. Budget completion before pricing it.

For each accepted risk, record a measurable threshold, the owner who watches it and the remedy that triggers.
Leave [UNDECIDED: acceptance thresholds and remedies] until the team has chosen them.

## The gacha design is done when

- [ ] The core loop works with the guaranteed non-paying roster.
- [ ] Banner timing, recurring income and the saving horizon use the same calendar.
- [ ] Rates, pity states, target guarantees, resets and carryover have one authoritative specification.
- [ ] Pity calculations link to economy.md and respect the assumptions of each formula.
- [ ] Duplicate outcomes, purchase prices and pack rounding are visible before purchase.
- [ ] Allowed products and rejected trust-breaking designs have explicit reasons.
- [ ] Daily time, stamina, absence and catch-up rules match the intended session.
- [ ] ARPU and ARPPU have a period, population, revenue basis and sourced target or an honest question marker.
- [ ] Scope includes release, rollback and support capacity.
- [ ] Every example number is labelled, every unresolved target is marked and every decision has rejected alternatives.
