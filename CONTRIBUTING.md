# Contributing

Pull requests that make the resulting design documents more decisive are welcome.

## What is accepted

| Kind | Examples |
|---|---|
| Fixes to an existing reference | A wrong formula, a stale reference number, a leading question that is not sharp |
| A new genre reference | `references/<genre>.md` for roguelike, survival, 4X, gacha, card battler |
| Translations | `i18n/<lang>/` for the README or a reference |
| Changes to `scripts/scaffold_gdd.py` | New sections or CSV tables; it must keep never overwriting an existing file |
| Worked examples | A full document set for an invented game under `examples/`, if you have the right to publish it |

## Writing rules

1. Every section answers four questions: what was decided, why, which alternatives were rejected, what the numbers are.
2. Prose in English. Every in-game name in English. Example names are invented, never taken from a shipped game's data.
3. Example numbers are labelled as examples, not values to copy.
4. Team size is never used as a reason to cut an idea outside a scope section.
5. Match the house style of `SKILL.md`: sentence-case headings, no decorative emoji, no em dashes, one thought per sentence, a table where readers compare, prose where they follow an argument.

## Steps

1. Fork and branch from `main`.
2. Make the change. If `scripts/` was touched, run the smoke test and unit tests:
   ```bash
   python scripts/scaffold_gdd.py /tmp/gdd-test --title "Test"
   python -m unittest scripts/test_scaffold_gdd.py
   ```
3. Open a pull request that says **what changed** and **why the resulting documents get better**. Keep it short.
4. A change to a reference cites at least one source: a shipped game, a postmortem, a GDC talk, an article.
