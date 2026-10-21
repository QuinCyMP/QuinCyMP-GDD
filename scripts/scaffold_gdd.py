#!/usr/bin/env python3
"""สร้างโครงชุดเอกสารออกแบบเกม พร้อมหัวข้อและตาราง CSV เปล่า

ใช้:
    python scaffold_gdd.py <โฟลเดอร์ปลายทาง> --title "ชื่อเกม"
    python scaffold_gdd.py ./design --title "Rustfall" --only 01,02,12,06

ทุกไฟล์ที่สร้างมีหัวข้อครบตามโครงมาตรฐาน และมีช่อง [ยังไม่ตัดสินใจ: ...] คาไว้
เพื่อให้ช่องว่างมองเห็นได้ แทนที่จะถูกกลบด้วยภาษาสวย ๆ

สคริปต์นี้ไม่เขียนทับไฟล์ที่มีอยู่แล้ว — เรียกซ้ำได้ปลอดภัย
"""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

TODO = "[ยังไม่ตัดสินใจ: {}]"

# slug -> (หัวข้อไฟล์, [ (หัวข้อย่อย, คำถามนำที่ต้องตอบ) ])
DOCS = {
    "00-one-pager": ("One-pager", [
        ("Logline", "ประโยคเดียว: แนว + จุดต่าง + ผู้เล่นทำอะไร"),
        ("เกมนี้คืออะไร", "สามย่อหน้า ย่อหน้าละไม่เกิน 4 บรรทัด"),
        ("ทำไมถึงต่าง", "The One Thing เทียบกับเกมจริง 2 ชื่อ"),
        ("ทำไมถึงมีคนเล่น", "ผู้เล่นเป้าหมายเล่นอะไรอยู่ และหงุดหงิดกับอะไร"),
        ("ภาพรวมตัวเลข", "world size / session length / time to endgame / concurrency"),
        ("สถานะและสิ่งที่ต้องการ", "มีอะไรแล้ว ต้องการอะไรจากผู้อ่าน"),
    ]),
    "01-vision": ("วิสัยทัศน์", [
        ("Pillars", "หลักตัดสินใจ 3 ข้อ ที่คมพอจะปฏิเสธของดี ๆ ได้"),
        ("The One Thing", "ในเกมนี้ผู้เล่น___ได้ ซึ่ง [เกมจริง] ทำไม่ได้เพราะ___"),
        ("ผู้เล่นเป้าหมาย", "ตอนนี้เล่นอะไร หงุดหงิดกับอะไร เล่นครั้งละกี่นาที"),
        ("ทำไมต้องมีผู้เล่นอื่น", "ระบบไหนพังทันทีถ้าเล่นคนเดียว"),
        ("อารมณ์เป้าหมาย", "10 นาทีแรก / ชั่วโมงที่ 10 / ชั่วโมงที่ 100"),
    ]),
    "02-core-loops": ("Core loops", [
        ("Moment loop (1–30 วินาที)", "กดอะไร เห็นอะไรตอบกลับ ตัดสินใจอะไร"),
        ("Session loop (20–90 นาที)", "เปิดเกมมาทำอะไรก่อน ปิดตอนไหนถึงรู้สึกคุ้ม"),
        ("Week loop", "อะไรทำให้กลับมาพรุ่งนี้ ที่ไม่ใช่ daily quest"),
        ("Lifetime loop", "อะไรคือจบ และหลังจากนั้นมีอะไร"),
    ]),
    "03-world": ("โลกและการสำรวจ", [
        ("ขนาดและเวลาเดินทาง", "km² / ความเร็ว m/s / เวลาข้ามโลก"),
        ("ความหนาแน่น", "ช่วงห่าง POI เป้าหมาย และจำนวน POI แยกตามชนิด"),
        ("Traversal", "verb การเดินทาง และผลต่อรูปร่างโลก"),
        ("Fast travel", "มีไหม ปลดล็อกอย่างไร ต้นทุนอะไร"),
        ("การแบ่งโซนและ gating", "level / skill / knowledge gate"),
        ("วิธีผลิตโลกที่ทีมขนาดนี้ทำไหว", "modular kit / procedural + landmark / โลกที่ผู้เล่นเปลี่ยน"),
    ]),
    "04-progression": ("Progression", [
        ("แหล่งความก้าวหน้า", "เลเวล / เกียร์ / สกิล / ความรู้ผู้เล่น / ชื่อเสียง"),
        ("Vertical หรือ horizontal", "เลือกอะไร และใครป้อนเนื้อหาให้"),
        ("เพดานและหลังเพดาน", "มี cap ไหม ถึงแล้วโตทางไหนต่อ"),
        ("ผู้เล่นใหม่ในปีที่ 2", "ไล่ทันไหม และควรไล่ทันไหม"),
        ("ตัวเลข", "ชั่วโมงถึง cap / อัตราส่วนพลัง endgame ต่อผู้เล่นใหม่ — ดู data/xp-curve.csv"),
    ]),
    "05-combat": ("ระบบต่อสู้", [
        ("รูปแบบ", "tab-target หรือ action — และเหตุผลที่ผูกกับ concurrency"),
        ("จังหวะ", "GCD / จำนวนปุ่มที่ใช้จริง / การตัดสินใจต่อวินาที"),
        ("ตัวเลข", "TTK ต่อ mob / TTK ผู้เล่นต่อผู้เล่น"),
        ("Role และการพึ่งพา", "ถ้ามี role ทำไมคนเดียวทำแทนไม่ได้"),
        ("ความตาย", "เสียอะไร กลับมานานแค่ไหน"),
    ]),
    "06-economy": ("เศรษฐกิจ", [
        ("Faucet", "เงินเข้าจากไหน g/ชม. เท่าไร — ดู data/economy-flow.csv"),
        ("Sink", "เงินออกทางไหน g/ชม. เท่าไร"),
        ("สมดุล", "faucet − sink ต่อเดือน คิดเป็นกี่ %"),
        ("ตลาดผู้เล่น", "bind หรือไม่ / ซื้อขายที่ไหน / ค่าธรรมเนียม / ขั้นต่ำที่ตลาดยังทำงาน"),
        ("เวลาเป็นสกุลเงิน", "ของสำคัญแต่ละชิ้นใช้เวลากี่ชั่วโมง"),
        ("ความเสี่ยงจากบอท", "กิจกรรมไหนที่บอททำคุ้มกว่าคน และกันอย่างไร"),
    ]),
    "07-social-mmo": ("สังคมและโครงสร้าง MMO", [
        ("Server topology", "shard / megaserver / single shard / instanced — และเหตุผล"),
        ("Concurrency", "คนต่อพื้นที่ / CCU เป้าหมาย"),
        ("ทำไมคนแปลกหน้าถึงร่วมมือกัน", "กลไกที่บังคับหรือจูงใจให้พึ่งพากัน"),
        ("การจับกลุ่มและกิลด์", "กิลด์ทำอะไรได้ที่กลุ่มเพื่อนทำไม่ได้"),
        ("การกันกริฟและชื่อเสียง", "ใครบังคับใช้ ระบบหรือผู้เล่น"),
        ("มวลวิกฤต", "ระบบไหนต้องการกี่คนขั้นต่ำ และต่ำกว่านั้นจะ degrade อย่างไร"),
    ]),
    "08-endgame-liveops": ("Endgame และ live ops", [
        ("300 ชั่วโมงแล้วทำอะไร", "รูปแบบ endgame หลัก"),
        ("อัตราการผลิตเทียบการบริโภค", "ทีมผลิตได้เดือนละเท่าไร ผู้เล่นหนักกินเดือนละเท่าไร"),
        ("เนื้อหาที่ผู้เล่นสร้างให้กัน", "ระบบไหนที่ผู้เล่นเติมเนื้อหาเอง"),
        ("จังหวะอัปเดต", "ทุกกี่สัปดาห์ ใครทำ"),
    ]),
    "09-monetization": ("โมเดลรายได้", [
        ("รูปแบบ", "B2P / subscription / F2P และเหตุผล"),
        ("ผลย้อนกลับต่อ design", "โมเดลนี้บังคับให้ออกแบบอะไรต่างไป"),
        ("สิ่งที่จะไม่ขายเด็ดขาด", "เส้นที่ไม่ข้าม และเหตุผล"),
        ("ตัวเลข", "ราคา / ARPU ที่สมเหตุสมผล / จุดคุ้มทุนค่า server"),
    ]),
    "10-art-audio": ("ทิศทางศิลป์และเสียง", [
        ("สไตล์ภาพ", "เลือกอะไร และเลือกเพราะทีมขนาดนี้ผลิตไหว"),
        ("งบทางเทคนิค", "จำนวน asset สำหรับ vertical slice / texture set / modular kit"),
        ("เสียง", "จำนวนแทร็ก จำนวน SFX ขั้นต่ำ"),
        ("ที่มาของภาพอ้างอิงทุกภาพ", "จำเป็นก่อนเอกสารออกสู่สายตาผู้ซื้อ"),
    ]),
    "11-tech-assumptions": ("ข้อกำหนดทางเทคนิคที่ design เรียกร้อง", [
        ("ผู้เล่นพร้อมกันในพื้นที่เดียว", "กี่คน"),
        ("Tick rate ที่ระบบต่อสู้ต้องการ", ""),
        ("ข้อมูลที่ต้องคงอยู่ถาวร", "inventory / ที่ดิน / ความสัมพันธ์ / สภาพโลก"),
        ("Server ตัดสินอะไร client ตัดสินอะไร", "ทุกอย่างที่แลกเป็นมูลค่าได้ = server เท่านั้น"),
        ("การโหลดโลก", "streaming / zone / instance"),
    ]),
    "12-scope-roadmap": ("ขอบเขตและลำดับการสร้าง", [
        ("Vertical slice", "เล็กที่สุดที่พิสูจน์ The One Thing — พื้นที่ ระบบ asset เวลา"),
        ("ลำดับการสร้าง", "ระบบไหนต้องมาก่อนเพราะระบบอื่นพึ่งมัน"),
        ("สิ่งที่ตัดออกในเวอร์ชันแรก", "พร้อมเงื่อนไขที่จะเอากลับมา"),
        ("แผนสำรองถ้าย่อ scope", "MMO เล็ก 100–500 คน จะหน้าตาอย่างไร"),
    ]),
    "13-risks": ("ความเสี่ยง", [
        ("ตารางความเสี่ยง", "เรียงตามผลกระทบ × โอกาส พร้อมสัญญาณเตือนและแผนรับมือ"),
    ]),
}

PITCH = {
    "pitch-deck-outline": ("โครง pitch deck", [
        ("สไลด์ 1–11", "ดู references/selling-the-design.md — อย่าลืมสไลด์ 'สิ่งที่ต้องการ'"),
    ]),
    "buyer-brief": ("บรีฟตามประเภทผู้รับ", [
        ("ผู้รับคือใคร", "A พับลิชเชอร์/นักลงทุน · B สตูดิโอ/ผู้ซื้อ IP · C ผู้ร่วมทีม"),
        ("เขาถามอะไรในใจ", ""),
        ("สิ่งที่ต้องเน้น", ""),
        ("สิ่งที่ต้องตัดออก", ""),
    ]),
}

CSV_HEADERS = {
    "xp-curve.csv": ["level", "xp_required", "xp_cumulative", "est_hours", "est_hours_cumulative"],
    "items.csv": ["id", "name_th", "name_en", "tier", "slot", "power", "value_g", "bind", "source"],
    "drop-tables.csv": ["mob_id", "item_id", "drop_rate", "min_qty", "max_qty", "pity_after"],
    "mob-stats.csv": ["id", "name", "level", "hp", "dps", "xp_reward", "gold_reward", "ttk_seconds"],
    "skills.csv": ["id", "name", "class", "cooldown", "cost", "damage_coeff", "unlock_level"],
    "economy-flow.csv": ["source_type", "name", "gold_per_hour", "player_level_band"],
}


def render(title: str, game: str, sections, slug: str) -> str:
    lines = [
        f"# {title}",
        "",
        f"> เกม: **{game}** · ปรับปรุงล่าสุด {date.today().isoformat()}",
        "",
    ]
    for heading, prompt in sections:
        lines.append(f"## {heading}")
        lines.append("")
        if prompt:
            lines.append(f"<!-- ต้องตอบ: {prompt} -->")
            lines.append("")
        lines.append(TODO.format(prompt or heading))
        lines.append("")
    if slug not in ("00-one-pager",):
        lines += [
            "## ทางเลือกที่พิจารณาแล้วตัดทิ้ง",
            "",
            "| ทางเลือก | ตัดทิ้งเพราะ |",
            "|---|---|",
            "| | |",
            "",
        ]
    return "\n".join(lines)


def write_if_absent(path: Path, content: str, created: list, skipped: list) -> None:
    if path.exists():
        skipped.append(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(path)


def main() -> int:
    ap = argparse.ArgumentParser(description="ตั้งโครงชุดเอกสารออกแบบเกม")
    ap.add_argument("target", help="โฟลเดอร์ปลายทาง เช่น ./design")
    ap.add_argument("--title", required=True, help="ชื่อเกม")
    ap.add_argument("--only", help="สร้างเฉพาะบางไฟล์ เช่น 01,02,12,06")
    args = ap.parse_args()

    root = Path(args.target)
    created: list = []
    skipped: list = []

    # ตัด leading zero ทิ้งทั้งสองฝั่ง เพราะบางเชลล์ (PowerShell) แปลง 01 เป็น 1 ให้เอง
    wanted = None
    if args.only:
        wanted = {p.strip().lstrip("0") or "0" for p in args.only.split(",") if p.strip()}

    for slug, (title, sections) in DOCS.items():
        if wanted and (slug.split("-")[0].lstrip("0") or "0") not in wanted:
            continue
        write_if_absent(root / f"{slug}.md", render(title, args.title, sections, slug), created, skipped)

    if not wanted:
        for slug, (title, sections) in PITCH.items():
            write_if_absent(root / "pitch" / f"{slug}.md", render(title, args.title, sections, slug), created, skipped)

        for name, headers in CSV_HEADERS.items():
            path = root / "data" / name
            if path.exists():
                skipped.append(path)
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8", newline="") as fh:
                csv.writer(fh).writerow(headers)
            created.append(path)

    for p in created:
        print(f"สร้าง  {p}")
    for p in skipped:
        print(f"ข้าม   {p} (มีอยู่แล้ว)")
    print(f"\nรวม: สร้างใหม่ {len(created)} ไฟล์, ข้าม {len(skipped)} ไฟล์")
    if created:
        print("ลำดับที่แนะนำให้เขียน: 01 → 02 → 12 → 06 แล้วค่อยไล่ที่เหลือ (00 เขียนท้ายสุด)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
