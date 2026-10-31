# Economy math

Read when writing `06-economy.md`, `04-progression.md`, or any table in `data/`. State the assumptions and units before using a formula. Numerical targets labelled as the author's rules of thumb are starting points to test, not observed industry ranges. Worked examples are illustrative, not values to copy. See [Sources and limits](#9-sources-and-limits) for what the cited games do and do not establish.

## 1. Faucet and sink

A game economy is a tank. **Faucets** pour currency in, **sinks** drain it out. Net currency creation measures the change in supply from those flows; it does not by itself measure the change in item prices.

```
net currency growth over a period = (total currency created − total currency destroyed) ÷ currency held at period start
price inflation over a period = (price index at period end ÷ price index at period start) − 1
```

Use totals for the same population and period, with a nonzero starting balance. Convert per-player hourly flows using the relevant player-hours before comparing them with a monthly target. Define the item basket and weights for a price index separately.

**Author's rule of thumb:** start by testing **0 to +5% net currency growth per month**, and investigate growth above **10%**. Neither figure is a demonstrated price-inflation threshold. Decide the target from population changes, production, prices and newcomer purchasing power; record why a different target was rejected. [EVE Online's January 2025 report](https://www.eveonline.com/news/view/monthly-economic-report-january-2025) discusses mineral, module and ship prices separately rather than establishing a universal safe growth band.

The table the document must carry:

| Faucet (in) | g/hr | | Sink (out) | g/hr |
|---|---|---|---|---|
| Normal mob hunting | 800 | | Gear repair | 260 |
| Vendor sales | 300 | | Travel fees | 90 |
| Daily quests | 400 | | Market fee (5%) | 180 |
| **Total** | **1,500** | | Consumables | 350 |
| | | | Land rent | 120 |
| | | | Failed crafting | 400 |
| | | | **Total** | **1,400** |

These numbers show the shape. They are not values to copy. Put the real game's numbers in.

Sinks that work, by effectiveness:

1. **Wear and repair.** Drains continuously with play and never feels like a tax.
2. **Transaction fees.** The busier the economy, the more it drains. Self-balancing.
3. **Consumables.** Potions, food, ammunition, temporary buffs.
4. **Failed crafts and upgrades.** Drains large sums, but watch how players feel about it.
5. **Status goods with no power.** Cosmetics, housing, titles. A sink that touches balance not at all.

Sinks that do not work: one-time purchases (drain once, then stop), and anything a player avoids by not doing that activity.

## 2. Drop rate and time to obtain

```
mean time to the item      E[t] = time per attempt ÷ drop rate
time at 90% confidence     t90  = time per attempt × ln(0.10) ÷ ln(1 − p)
```

Example: 1% drop, 90 seconds per kill.

- Mean: 90 ÷ 0.01 = 9,000 s = **2.5 hours**.
- 90% of players have it within 90 × ln(0.1) ÷ ln(0.99) = **5.7 hours**.
- The unluckiest 1% still lack it after **11.5 hours**. Those are the players writing the forum posts.

**Author's rule of thumb:** when t90 exceeds **10 hours**, consider a **pity system** (a counter that guarantees the drop within N attempts). This is a design review trigger, not an empirically established trust threshold. Decide the maximum acceptable unlucky-player time and why pity or another acquisition path fits it. [HoYoverse's guarantee explanation](https://support.hoyoverse.com/hc/en-us/articles/50333940684953-How-does-the-Wish-guarantee-system-work) gives an attempt-based guarantee, not a ten-hour rule; earning attempts and making attempts need separate time budgets.

```
Pity: after attempt N, the drop rate rises by x% per attempt until it reaches 100% at attempt M
```

## 3. XP curve

Three candidate shapes. The result goes to `data/xp-curve.csv`. The exponent ranges and pacing targets below are the author's rules of thumb, not sourced player-behaviour benchmarks.

| Shape | Formula | Feel |
|---|---|---|
| Linear | `XP(n) = a × n` | Late levels come too fast, nothing has weight |
| Polynomial | `XP(n) = a × n^b` (b ≈ 1.5 to 2.5) | A starting candidate; evaluate alongside XP earned per hour. |
| Exponential | `XP(n) = a × r^n` (r ≈ 1.1 to 1.2) | Late levels become a wall. Handle with care. |

Always check the curve in **time**, never in XP alone:

```
hours per level(n) = XP(n) ÷ (XP earned per hour at that level)
```

**Author's rules of thumb:** early levels in minutes, mid-game **1 to 3 hours** each, late game **5 to 15 hours** each. Review intermediate goals if the last level takes more than **40 hours**. Choose pacing against the target player's session budget and record why faster or slower alternatives were rejected.

## 4. Power curve and balance

```
Power ≈ (damage per second) × (damage that can be absorbed)
```

The two sides multiply. Raising damage by 20% and health by 20% makes a character 44% stronger, not 20%. That is why gear granting both explodes balance faster than expected.

Ratios the document must state:

- Endgame player power ÷ new player power: **10× to 50×** is the author's rule-of-thumb starting range, with **100×** a review trigger, not a proven grouping limit. Test shared encounters and any level scaling before choosing the ratio.
- Power gap between adjacent gear tiers: **10 to 20%** per tier is also the author's rule of thumb. State whether the percentage applies to DPS, survivability or their product; record why a different gap was rejected.
- The level range within which players can still group. It decides whether two friends at different levels can play together.

[ArenaNet's Mastery design](https://www.guildwars2.com/en/news/reimagining-progression-the-mastery-system/) is a comparison for progression through new capabilities rather than repeated gear growth. It does not validate the ratios above or measure endgame-to-new-player combat power.

## 5. Player market and liquidity

If players trade with each other, answer these:

| Question | Why it matters |
|---|---|
| Are items bound on pickup? | Bound means no market. Unbound means a living market, and bots. |
| How many players until the market has liquidity? | The author's rule of thumb is to review liquidity below roughly 500 CCU. Measure active traders, listing depth and time to sale per item; CCU alone is not a failure threshold. |
| Where is trade done? | Player listings (slow, social) or an auction house (fast, anonymous). The choice changes the game's whole culture. |
| What is the fee? | A potential sink. 3 to 8% is the author's rule-of-thumb starting range, not an industry norm. Include listing and sale fees separately; see the Guild Wars 2 counterexample in Sources and limits. |
| Are rare items actually finite? | Anything producible without limit always falls to zero. |

**Author's rule of thumb:** below **500 CCU**, compare a player-only market with NPC-supported trade rather than assuming either will work. Choose using observed sale times and demand. Record why the rejected model fails, and account for currency created by any NPC floor price.

## 6. Time is the real currency

Everything in the game has a price in **player hours**. The document always carries a table like this illustrative example. The hours and intended audiences below are invented targets, not measured player percentiles:

| Item | Hours needed | Who reaches it |
|---|---|---|
| Full mid-tier gear set | 15 h | Everyone |
| Full endgame gear set | 120 h | Regular players |
| Rarest item | 400+ h | A hypothetical top 2% of players by play time; verify against the actual population |

Then compare with the **target player's real play time**. In an illustrative schedule of 6 hours per week, 120-hour endgame gear takes 20 weeks, roughly 5 months. Decide whether that fits the audience and record why a shorter or longer target was rejected.

## 7. Files that belong in `data/`

| File | Columns |
|---|---|
| `xp-curve.csv` | `level, xp_required, xp_cumulative, est_hours, est_hours_cumulative` |
| `items.csv` | `id, name, tier, slot, power, value_g, bind, source` |
| `drop-tables.csv` | `mob_id, item_id, drop_rate, min_qty, max_qty, pity_after` |
| `mob-stats.csv` | `id, name, level, hp, dps, xp_reward, gold_reward, ttk_seconds` |
| `skills.csv` | `id, name, class, cooldown, cost, damage_coeff, unlock_level` |
| `economy-flow.csv` | `source_type (faucet or sink), name, gold_per_hour, player_level_band` |

Column headers are always English and snake_case, because these files are imported into the engine directly and most tools break on anything else. Localised display names get their own column (`name_<lang>`) when the game ships in several languages.

## 8. Sanity check before delivery

- [ ] Monthly net currency growth and price inflation are measured separately; the chosen targets have reasons and rejected alternatives.
- [ ] Every rare item has its t90 computed under stated assumptions; the pity decision follows the chosen unlucky-player time budget.
- [ ] The xp curve converted to hours looks sane.
- [ ] Endgame-to-new-player and adjacent-tier power ratios are explicit and tested against the intended grouping experience.
- [ ] The market works at the real target player count.
- [ ] Every activity with guaranteed income was checked: a bot must not out-earn a human.

## 9. Sources and limits

These primary sources provide comparisons, not universal tuning targets. Source pages checked on 2026-10-31. Keep each game's mechanism separate from the author's rules of thumb above.

| Topic | Source and what it establishes | Limit of the evidence |
|---|---|---|
| Currency growth and prices | [EVE Online, Monthly Economic Report, January 2025](https://www.eveonline.com/news/view/monthly-economic-report-january-2025) reports a 7.7% monthly increase in its mineral price index and separately discusses module and ship prices. | A category price change does not establish a safe aggregate inflation rate or a net currency-growth target. The 0 to +5% target and 10% review trigger remain the author's rules of thumb. |
| Pity | [HoYoverse, How does the Wish guarantee system work?](https://support.hoyoverse.com/hc/en-us/articles/50333940684953-How-does-the-Wish-guarantee-system-work) describes a Character Event Wish guarantee of a 5-star character within 90 wishes, with the counter resetting on a 5-star result. | This supports an attempt-based cap, not the 10-hour review trigger or a guarantee of a specific character on that attempt. The time trigger remains the author's rule of thumb. |
| Power progression | [ArenaNet, Reimagining Progression: The Mastery System](https://www.guildwars2.com/en/news/reimagining-progression-the-mastery-system/) describes endgame growth through capabilities instead of grinding for gear. | It supplies no comparable DPS-times-survivability ratios. The 10× to 50× range, 100× trigger and 10 to 20% tier gap remain the author's rules of thumb. |
| Market fees | [ArenaNet support, Where is my gold? (German)](https://help.guildwars2.com/hc/de/articles/222384087-Wo-ist-mein-Gold) lists a 5% nonrefundable listing fee and a 10% sale fee, each based on the price. | Together these deduct 15% on a completed listing, before rounding effects. This is a counterexample to treating 3 to 8% as a universal range; it does not establish the best fee for another game. |
| XP pacing and market population | No empirical source is asserted for these targets. | The exponent ranges, hours-per-level ranges, 40-hour review trigger and 500-CCU review trigger are the author's rules of thumb. Replace them with measured pacing and liquidity targets for the project. |
