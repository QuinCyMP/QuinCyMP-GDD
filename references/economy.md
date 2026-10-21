# Economy math

Read when writing `06-economy.md`, `04-progression.md`, or any table in `data/`. Every formula here works as is: put numbers in, get an answer that goes straight into the document.

## 1. Faucet and sink

A game economy is a tank. **Faucets** pour currency in, **sinks** drain it out. When inflow exceeds outflow for long, inflation breaks the system, and it always happens unless designed against.

```
inflation rate = (Σ faucet per player per hour − Σ sink per player per hour) ÷ average currency held
```

A target that works: **faucet − sink ≈ 0 to +5% per month**. Slightly positive beats exactly zero because new players need currency flowing in, but above 10% per month prices run away from new players until they cannot join.

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

Rule to write into the document: when t90 exceeds 10 hours, add a **pity system** (a counter that guarantees the drop within N attempts). Without one, perceived unfairness destroys trust.

```
Pity: after attempt N, the drop rate rises by x% per attempt until it reaches 100% at attempt M
```

## 3. XP curve

Three shapes in real use. The result goes to `data/xp-curve.csv`.

| Shape | Formula | Feel |
|---|---|---|
| Linear | `XP(n) = a × n` | Late levels come too fast, nothing has weight |
| Polynomial | `XP(n) = a × n^b` (b ≈ 1.5 to 2.5) | **The best default.** Steady progress. |
| Exponential | `XP(n) = a × r^n` (r ≈ 1.1 to 1.2) | Late levels become a wall. Handle with care. |

Always check the curve in **time**, never in XP alone:

```
hours per level(n) = XP(n) ÷ (XP earned per hour at that level)
```

A good shape: early levels in minutes, mid-game 1 to 3 hours each, late game 5 to 15 hours each. If the last level takes more than 40 hours, add intermediate goals along the way.

## 4. Power curve and balance

```
Power ≈ (damage per second) × (damage that can be absorbed)
```

The two sides multiply. Raising damage by 20% and health by 20% makes a character 44% stronger, not 20%. That is why gear granting both explodes balance faster than expected.

Ratios the document must state:

- Endgame player power ÷ new player power: **10× to 50×** works. Above 100× new and veteran players can no longer play together, which kills the MMO.
- Power gap between adjacent gear tiers: **10 to 20%** per tier.
- The level range within which players can still group. It decides whether two friends at different levels can play together.

## 5. Player market and liquidity

If players trade with each other, answer these:

| Question | Why it matters |
|---|---|
| Are items bound on pickup? | Bound means no market. Unbound means a living market, and bots. |
| How many players until the market has liquidity? | Below roughly 500 CCU a free market usually fails; NPCs must support it. |
| Where is trade done? | Player listings (slow, social) or an auction house (fast, anonymous). The choice changes the game's whole culture. |
| What is the fee? | The main sink. 3 to 8% is the normal range. |
| Are rare items actually finite? | Anything producible without limit always falls to zero. |

Small-team rule: a free market needs critical mass. With a CCU target below 500, design a semi-NPC market (NPCs buy at a floor price), or players cannot sell and quit.

## 6. Time is the real currency

Everything in the game has a price in **player hours**. The document always carries this table:

| Item | Hours needed | Who reaches it |
|---|---|---|
| Full mid-tier gear set | 15 h | Everyone |
| Full endgame gear set | 120 h | Regular players |
| Rarest item | 400+ h | Top 2% |

Then compare with the **target player's real play time**. At 6 hours per week, 120-hour endgame gear is 5 months, which may be too long or just right, but it must be a **decision**, not an accident.

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

- [ ] Total faucet − total sink is within 0 to +5% per month.
- [ ] Every rare item has its t90 computed, and anything above 10 hours has pity.
- [ ] The xp curve converted to hours looks sane.
- [ ] Endgame-to-new-player power ratio is within 10× to 50×.
- [ ] The market works at the real target player count.
- [ ] Every activity with guaranteed income was checked: a bot must not out-earn a human.
