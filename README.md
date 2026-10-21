# QuinCyMP GDD

**สกิลสำหรับ AI coding agent (Claude Code, Codex, OpenCode) ที่เขียนเอกสารออกแบบเกม (GDD) ให้ "ตัดสินใจ" ไม่ใช่ "บรรยาย"**

*An agent skill that writes game design documents that record decisions instead of describing dreams. Thai prose, English names for everything in-game. Specialised in MMORPG and open-world design, usable for any genre.*

> เอกสารออกแบบคือบันทึกการตัดสินใจ ไม่ใช่คำบรรยายความฝัน
> ทุกหัวข้อต้องตอบ 4 อย่าง: **ตัดสินใจว่าอะไร / เพราะอะไร / ตัดทางเลือกไหนทิ้ง / ตัวเลขเท่าไร**

## ทำอะไรได้ / What it does

| งาน | ผลลัพธ์ |
|---|---|
| เริ่มออกแบบเกมจากศูนย์ (เฟส A) | ล็อก 5 ข้อใหญ่ก่อน แล้วตั้งโครงเอกสาร 14 ไฟล์ + pitch + ตาราง CSV ด้วย `scripts/scaffold_gdd.py` |
| ต่อยอดโปรเจกต์ที่มีเอกสารอยู่แล้ว (เฟส B) | ตรวจความขัดแย้ง ลิงก์ และ "บ้านหลัก" ของทุกกฎ ก่อนเพิ่มของใหม่ (`references/living-vault.md`) |
| ออกแบบคลาส อาชีพ สกิล | เกณฑ์ผ่าน 5 ข้อ ข้อห้าม 9 ข้อ research 4 ช่อง (`references/class-and-skill-design.md`) |
| บาลานซ์เศรษฐกิจ | สูตร faucet/sink, drop rate, xp curve, เงินเฟ้อ ใส่ตัวเลขแล้วได้คำตอบทันที (`references/economy-math.md`) |
| โลก open world | ขนาดโลก ความหนาแน่น POI traversal การแบ่งโซน (`references/open-world.md`) |
| ระบบ MMO | server topology, progression, social, endgame, monetization (`references/mmo-systems.md`) |
| ขายหรือ pitch | โครง pitch deck 11 สไลด์ และบรีฟแยกตามผู้รับ (`references/selling-the-design.md`) |

## ติดตั้ง / Install

**Claude Code** (ทั้งเครื่อง / global):

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD ~/.claude/skills/quincymp-gdd
```

**Claude Code** (เฉพาะโปรเจกต์ / per project):

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD .claude/skills/quincymp-gdd
```

**Codex / agents ที่อ่าน `.agents/skills/`:**

```bash
git clone https://github.com/QuinCyMP/QuinCyMP-GDD .agents/skills/quincymp-gdd
```

**ผ่าน skills CLI:**

```bash
npx skills add QuinCyMP/QuinCyMP-GDD
```

## ใช้งาน / Usage

พิมพ์กับ agent ได้เลย เช่น

- "อยากทำเกม MMO แนว survival ช่วยคิดระบบ"
- "เขียน GDD ให้เกมนี้"
- "บาลานซ์ดาเมจ / คิดระบบ crafting / ออกแบบคลาส"
- "ขายไอเดียเกมนี้ให้พับลิชเชอร์"

สกิลจะถามคำถามที่ต้องตอบก่อนเขียน และทำเครื่องหมาย `[ยังไม่ตัดสินใจ: ...]` ทุกช่องที่ยังไม่มีคำตอบ แทนการกลบด้วยภาษาสวย ๆ

ตั้งโครงเอกสารด้วยมือ:

```bash
python scripts/scaffold_gdd.py ./design --title "ชื่อเกม"
python scripts/scaffold_gdd.py ./design --title "ชื่อเกม" --only 01,02,12,06
```

สคริปต์ไม่เขียนทับไฟล์ที่มีอยู่ เรียกซ้ำได้ปลอดภัย ไม่ต้องติดตั้งอะไรเพิ่ม (Python 3.8+ standard library)

## โครงสร้าง / Layout

```
SKILL.md                         กติกาหลัก เฟส A/B และสิ่งที่ทำให้ GDD ดูสมัครเล่น
references/
  phase-a-bootstrap.md           เริ่มจากศูนย์: 5 ข้อที่ต้องล็อกก่อน
  gdd-structure.md               โครง 14 ไฟล์ พร้อมคำถามนำรายหัวข้อ
  living-vault.md                ต่อยอดของเดิมโดยไม่ทำให้ของเก่ากลายเป็นเท็จ
  class-and-skill-design.md      คลาส อาชีพ สกิล
  economy-math.md                สูตรเศรษฐกิจและตัวเลข
  open-world.md                  โลกและการสำรวจ
  mmo-systems.md                 ระบบเฉพาะแนว MMO
  selling-the-design.md          pitch และการขาย
scripts/
  scaffold_gdd.py                ตั้งโครงชุดเอกสาร + CSV
```

## ภาษา / Language

คำอธิบายทั้งหมดเป็นภาษาไทย ชื่อของทุกอย่างในเกมเป็นภาษาอังกฤษ เพราะชื่อในเอกสารต้องเป็นชื่อเดียวกับที่จะอยู่ในโค้ด
Contributions in English are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) · © 2026 QuinCyMP
