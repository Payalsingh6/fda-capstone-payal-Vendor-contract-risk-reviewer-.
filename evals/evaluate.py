import json
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent

# Try both .jsonl (L) and .json1 (1) - handles typo
for name in ["golden.jsonl", "golden.json1", "golden.json"]:
    for folder in [BASE, ROOT, Path("C:/capstone/evals"), Path("C:/capstone")]:
        p = folder / name
        if p.exists():
            GOLDEN_PATH = p
            break
    else:
        continue
    break
else:
    GOLDEN_PATH = BASE / "golden.jsonl"

for name in ["eval_config.json"]:
    for folder in [BASE, ROOT, Path("C:/capstone/evals"), Path("C:/capstone")]:
        p = folder / name
        if p.exists():
            CONFIG_PATH = p
            break
    else:
        continue
    break
else:
    CONFIG_PATH = BASE / "eval_config.json"

print(f"Using golden: {GOLDEN_PATH}")

def load_golden():
    records = []
    with open(GOLDEN_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    print("=== Day 04 Evaluator ===")
    golden = load_golden()
    config = load_config()
    print(f"Loaded {len(golden)} examples")
    risks = [r.get("expected_risk","UNK") for r in golden]
    print(Counter(risks))
    out = BASE / "eval_results.json"
    with open(out, "w") as f:
        json.dump({"total": len(golden), "risks": dict(Counter(risks))}, f, indent=2)
    print(f"Saved to {out}")

if __name__ == "__main__":
    main()