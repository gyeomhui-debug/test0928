import csv, json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "장데이터.json"
keyword = sys.argv[1] if len(sys.argv) > 1 else input("검색 키워드: ").strip()

with DATA.open(encoding="utf-8") as f:
    rows = json.load(f)

result = [r for r in rows if keyword.lower() in (r.get("제목", "") + " " + r.get("본문", "")).lower()]
safe = re.sub(r'[\\/:*?"<>|]+', '_', keyword).strip() or "전체"
out = BASE / f"검색결과_{safe}.csv"

with out.open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["장", "제목", "본문"])
    w.writeheader(); w.writerows(result)

print(f"[OK] {len(result)}건 저장 → {out.name}")
for r in result:
    print(f"- 제{r['장']}장 {r['제목']}")
