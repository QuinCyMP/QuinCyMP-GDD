# Classes, jobs and skills

Read this before writing any ability the player chooses: classes, jobs, build paths, skills, perks.

## 0. Diagnose first: count the verbs

Before editing anything, count the verbs used to describe every ability and sort them by frequency. A real result from a draft with 510 abilities:

| Verb | Count |
|---|---:|
| **design** | **32** |
| make, build | 22 |
| **coordinate** | **13** |
| **inspect** | **8** |

Those are a consultant's verbs, not a game's. Strike, shoot, push, pull, throw, seize, breach, drag: none of them in the top group. When the count looks like this, the problem is not a few abilities but the whole set written in the wrong register. Rebuild it; do not patch entries one by one.

A second gauge: divide the ability count by the class count. If every class lands on exactly 2.0, the author filled a quota instead of writing what each class really has.

## 1. Step 0: research, never skipped

> If we do not look at what others built, we can only write what we have played, and what we have played is what everyone else has played too.

Look at all four shelves. One shelf alone gives a half class.

| Shelf | What it answers |
|---|---|
| **MMORPG** | **Job structure and the player economy.** Who depends on whom, who sells what to whom. |
| **ARPG, action RPG** | **Item and stat mechanics.** Upgrades, sockets, quality, how stats divide the work. |
| **Anime, manga** | **The job's identity and its price.** Why people fear or respect it. |
| **Novels, myth** | **Its place in society.** Where the job stands in the world, beyond which buttons it presses. |

The first two shelves answer mechanics, the last two answer identity. A class with only mechanics is a spreadsheet; a class with only identity is a short story.

Three things to bring back:

| | Find | Use |
|---|---|---|
| 1 | **Mechanics other games made work** | Adapt, never copy, and record the source with an ID that can be traced back |
| 2 | **Mechanics other games failed at, or cannot do** | **This is where a monopoly comes from.** The strongest hook is rarely "we do it better"; it is "we can, while the whole genre cannot". One ARPG makes socketed runes permanent, so a class that can **remove runes** is something the genre does not have. |
| 3 | **Mechanics that conflict with our rules** | Write them under "Alternatives considered and rejected" with the reason, so nobody proposes them again |

Record research in one sources file with two separate columns per row: **what the source actually says** and **what we decided to take from it**. Class files cite the row's ID. Without that, in six months nobody knows why the design looks the way it does.

## 2. Five criteria every ability passes

| | Criterion | Test question |
|---|---|---|
| 1 | **It is a player verb** | Does the player do something, or merely "have a property"? |
| 2 | **It is visible** | Does a bystander know something happened? |
| 3 | **Someone else gains or loses** | Does it touch the world or another player? |
| 4 | **At least one thing no other class can do** | Without it, this class is a reskin |
| 5 | **It has a price** | Cost, time, materials, risk, or dependence on another player |

Rulings that serve as precedent:

| Proposal | Ruling | Why |
|---|---|---|
| *Separate a weapon's frame from its modules for maintenance* | Pass | **Visible.** The weapon comes apart into two pieces in front of everyone. |
| *Check compatibility before assembling* | Fail | **Invisible and unnecessary.** That is a tooltip, not an ability. |

## 3. Nine things that are never a skill

| Never | Because | Instead |
|---|---|---|
| **Inspect, check, assess** on its own | UI, not a verb | A by-product of another skill |
| **Design a standard, set up a system** | The player does nothing | Write the **thing that gets produced** |
| **Teach, train the next generation** | If a mentor system exists, **every class can use it** | Cut it; it is nobody's hook |
| **Coordinate, queue** | Players already do it in chat | Write the **tool** that makes coordination possible |
| **Found an organisation, establish an institution** | One button cannot found anything | Write the **right** it unlocks to go and do it |
| **Anything the UI already shows everyone** | The skill grants nothing | Cut it |
| **A duplicate of another skill in the same class** | Equip both and the effects overlap: a wasted slot | Merge into one |
| **A game concept, not a class ability** | If everyone can do it by the rules, **it is a rule, not a skill** | Move it to the system file |
| **A boost that creates "lucky" outcomes** | If the game says enough mastery guarantees success, **luck has nowhere to act** | Make it **improve the result**, not the success chance |

The last row matters more than it looks. When the game declares a system free of randomness, luck-related stats disappear from every class that uses that system, along the whole branch, not just from the skill.

## 4. Three buckets people confuse

| | What it is | How it grows |
|---|---|---|
| **Library** | What the character **knows** | Grows every rank, accumulates |
| **Slots** | What the body **can use at once**, passives included | Grows slower than the library |
| **Bar** | Buttons that **can be pressed in a fight**, actives only | Usually fixed for the whole game |

> The library must grow faster than the slots, or there is no decision.

Reference numbers that work:

| Rank | New skills | Library | Slots | Must leave out |
|---|---:|---:|---:|---:|
| **1, start** | 12 to 14 | ~13 | **all** | **0, everything equipped** |
| **2** | +9 to 12 | ~22 | 16 | 6 |
| **3** | +8 | ~30 | 19 | 11 |
| **4** | +3 to 4 | ~33 | 21 | 12 |
| **5** | +3 to 4 | ~36 | 23 | 13 |

| Rank | Intended feeling |
|---|---|
| **1** | "I learned everything this job can do." No wrong decision before the player knows anything. |
| **2** | **The point where two players of the same class start to differ.** |
| **3 to 5** | Fewer new things, **but each one changes how the class is played**, not small additions piling up. |

The counts are not quotas. If a class really has 9 things, give it 9 and lower the slots.

## 5. The skill table: seven columns

```
| # | Skill | A/P | Growth | Formula | Type | Does |
```

| Column | Values |
|---|---|
| **A/P** | `A` active, pressed · `P` passive, always on |
| **Growth** | `none` fixed once learned · `Lv` gains EXP from use · `Rank` stronger on promotion |
| **Formula** | `none` · `Lv` · `Lv · STR` · `× <Stat>` · `by rank` · `caster Stat` · `% target Stat` |
| **Type** | `self` · `target` · `single` · `AOE` · `DoT` · `area` · `craft` |

**Formula** is the column people forget, and it solves a large problem. It is not there to hold a formula; it is there to **prevent double counting**. A skill reads a raw Attribute or a derived Stat, but only one of the two, or a bonus gets counted twice. Never put real numbers in this column: `Lv · STR` is enough, the multiplier lives in the balance file. Filling every cell with numbers bloats the file without adding a decision. Free benefit: scan the column down a whole rank and you see at once which Attribute no skill reads.

`× <Stat>` is the easiest pattern for building a monopoly. A multiplier on top of a finished Stat means "any class can raise this Stat, but this class multiplies it once more, so it beats everyone with the same points". Visible, measurable, and no new system needed.

Descriptions:

| Rejected | Accepted |
|---|---|
| `Sword slash, 1,000 damage + 20% of STR` | **`Cleave`**: a sword strike that damages enemies |
| `Repair armor +30 durability` | **`Mend`**: restores durability to worn gear |

Numbers appear in a description only when they *are* the design decision ("not supported above rank X", "1-week cooldown"), tagged `[PROVISIONAL: ...]`.

## 6. Class Attributes: five rules

If every character starts equal, the Attribute line is not decoration. It is advice on where to put points so this class's skills work at full strength.

| | Rule | Why |
|---|---|---|
| 1 | **Every value the skills run on is read by a real skill**, checked against the Formula column of **every** skill this rank can reach | A value no skill reads is a point the table forces the player to waste |
| 1b | **Except survival values** (HP, Stamina), which help without a skill reading them, **but the file must say where this rank is forced to take damage** | Applying rule 1 literally strips health from every class, which is wrong |
| 2 | **The set changes by rank and by branch, and should** | If the set never changes, choosing a branch does not change where points go |
| 3 | **Three or four values** | More than four means the class does not know what it does |
| 4 | **A value added at a high rank names the skill that caused it**, in one line under the table, never silently | |

> A good example: one branch keeps endurance and adds health (because high ranks are forced to stand mid-field). The other drops endurance for intellect (because its skills become magic). That is the point where two players of one class put points in different places for good.

## 7. Boundaries between close classes

Close classes always write over each other unless the boundary is drawn first. A real case: a defensive class and an offensive class both owned the words "formation" and "signal" in four places.

Find a **mechanical axis, not a theme**. "Defend versus attack" fixes nothing, because both still arrange formations.

| Axis that works | Example |
|---|---|
| **Raise our side versus lower theirs** | One intercepts, one cracks armor. **Same effect, opposite mechanics.** |
| **Who chooses who gets hurt** | One goes to the target; the other is chosen by the enemy |
| **Does the damage travel** | Reaches people versus happens only where they stand |
| **Control space versus control timing** | Who stands where versus when to engage |

Then make it machine-checkable. Put the boundary table at the top of **both** files, identical text, ending with:

```markdown
| **Words banned in this file** | "intercept" · "shield" | "signal" · "command" |
```

and `grep` tells you whether the boundary still holds. Side effect of a good boundary: the two classes counter each other without being designed to. A class that lowers defence naturally counters a class that relies on a health pool. That is the evidence the boundary works.

## 8. Procedure, in this order every time

| Step | Do | Skipped, you get |
|---|---|---|
| **0** | **Research all four shelves** (section 1) | Classes like games already played, with no skill anyone remembers came from this game |
| **1** | **Ask what the game's systems have and lack** | Skills that cite missing systems and a file torn out later |
| **2** | **Find the class's monopoly**, at least one per branch | A class that does many things and is necessary for none |
| **3** | **Write every node's single hook before any skill** | Skills pile up with no direction |
| **4** | **Draw boundaries with close classes** (section 7) | Two files using one word with nobody noticing |
| **5** | Finish rank 1 **before branching** | Branches with duplicate skills |
| **6** | Give rank 2 **more skills than slots** | Every player of this class identical |
| **7** | High ranks: **few things that change play**, plus named upgrades of old skills | High ranks become bigger numbers |
| **8** | **Cut with the nine prohibitions**, then count | Quota met, half of it meaningless |
| **9** | **Set slots from what actually remains** | A bloated file with no added decision |

Questions for the owner before every class:

1. **What does this class monopolise?** Which function nobody else can replace.
2. **Which systems does it depend on that are not yet written down?**
3. **How many branches?** Decided per class, never in advance, and only after every node's hook is written.

## 9. Done means, per class

| | Check |
|---|---|
| 1 | Every skill passes the **five criteria** |
| 2 | Nothing from the **nine prohibitions** remains |
| 3 | Every node has **one hook**, unique within the class |
| 4 | **Every branch has at least one monopoly skill** |
| 5 | Every skill fills **all seven columns** |
| 6 | High ranks have **new skills** and **at least two old skills made stronger**, described visibly, not as +% |
| 7 | The Active/Passive ratio **matches how the class actually works**; desk jobs lean passive |
| 8 | Every number is tagged `[PROVISIONAL: ...]` |
| 9 | **Read two adjacent branch hooks and you can choose without seeing a number** |
| 10 | **Every Attribute value is read by a skill**, survival values excepted with a written reason |
| 11 | **At least one research source cited**, all four shelves covered |
| 12 | **"Alternatives considered and rejected"** exists, including rejections from research |
| 13 | **Banned boundary words** have not leaked into skill text |
| 14 | Index, map and front matter updated if the node count changed |

## 10. Keep the standard inside the project

After the first class is finished, write a standards file in the project itself and name which class is the **reference file**. Rules tuned to this game beat generic rules, and the remaining dozens of classes come out looking alike. When the rules misfire on a real file, fix the rules. Do not bend the file to fit them.
