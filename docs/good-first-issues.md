# รายการ issue ที่จะเปิดหลัง push (good first issue)

> ไฟล์นี้เป็นร่างสำหรับเจ้าของ repo ใช้สร้าง issue บน GitHub ลบได้เมื่อสร้างครบ

| # | หัวข้อ | ป้าย | รายละเอียดสั้น |
|---|---|---|---|
| 1 | README ภาษาอังกฤษฉบับเต็ม | `documentation` `good first issue` | แปล README.md เป็น `README.en.md` ให้ครบทุกหัวข้อ |
| 2 | เพิ่ม reference แนว roguelike / roguelite | `enhancement` `good first issue` | `references/roguelike.md`: run structure, meta-progression, seed, ตัวเลข run length |
| 3 | เพิ่ม reference แนว survival / crafting | `enhancement` `good first issue` | hunger/thirst tick, base building, ตารางวัตถุดิบ |
| 4 | เพิ่ม reference แนว gacha / live service mobile | `enhancement` `good first issue` | pity, banner cadence, ARPU, อะไรขายได้ไม่ได้ |
| 5 | เพิ่ม reference แนว card battler / deckbuilder | `enhancement` `good first issue` | deck size, mana curve, rarity distribution |
| 6 | เพิ่ม reference แนว 4X / grand strategy | `enhancement` | turn economy, snowball control, victory conditions |
| 7 | scaffold: option `--lang en` ให้หัวข้อเป็นอังกฤษ | `enhancement` `good first issue` | เพิ่ม dict หัวข้อภาษาอังกฤษใน `scripts/scaffold_gdd.py` |
| 8 | scaffold: option `--genre` เลือกชุดไฟล์ | `enhancement` | เช่น `--genre roguelike` สร้างเฉพาะไฟล์ที่แนวนั้นต้องการ |
| 9 | ตัวอย่าง GDD จริงใน `examples/` | `help wanted` | เกมสมมติ 1 เกม เขียนครบ 14 ไฟล์ตามกติกา |
| 10 | unit test สำหรับ scaffold_gdd.py | `good first issue` | ทดสอบ: ไม่เขียนทับ, `--only` กรองถูก, CSV header ครบ |
| 11 | ตรวจสูตรใน economy-math.md กับแหล่งอ้างอิงจริง | `documentation` | เทียบกับ postmortem / GDC talk แล้วใส่ลิงก์อ้างอิง |
| 12 | GitHub Action: รัน scaffold smoke test ทุก PR | `ci` `good first issue` | workflow เรียก `python scripts/scaffold_gdd.py /tmp/x --title T` |
| 13 | แปล SKILL.md เป็นอังกฤษใน `i18n/en/` | `documentation` `help wanted` | สำหรับทีมต่างชาติที่อยากใช้กติกาเดียวกัน |
| 14 | checklist "ตรวจงานก่อนส่งมอบ" เป็นไฟล์แยกให้ copy ได้ | `good first issue` | `references/delivery-checklist.md` |
| 15 | เพิ่มคำถามนำสำหรับเกม co-op 2 ถึง 4 คน ใน gdd-structure | `enhancement` | หัวข้อ 07 ปัจจุบันเน้น MMO อย่างเดียว |

## วิธีเปิด issue ให้คนอยากช่วย

- ใส่ป้าย `good first issue` และ `hacktoberfest` ในเดือนตุลาคม
- ระบุไฟล์ที่ต้องแตะ และ "ผลลัพธ์ที่ถือว่าเสร็จ" 1 ถึง 2 บรรทัด
- ตอบ PR ภายใน 1 ถึง 2 วัน
