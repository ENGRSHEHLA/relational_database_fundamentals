from collections import Counter
import json
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "query.json"
OUTPUT_FILE = BASE_DIR / "bar_chart.png"


def load_major_counts(path: Path) -> Counter:
    with path.open("r", encoding="utf-8") as file_handle:
        students = json.load(file_handle)

    majors = [student.get("major") or "Unknown" for student in students]
    return Counter(majors)


def main() -> None:
    major_counts = load_major_counts(DATA_FILE)
    majors = sorted(major_counts)
    counts = [major_counts[major] for major in majors]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(majors, counts, color="#3b82f6", edgecolor="#1e3a8a")
    plt.title("Student Count by Major")
    plt.xlabel("Major")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()

    for bar, count in zip(bars, counts):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            str(count),
            ha="center",
            va="bottom",
        )

    plt.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Saved chart to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()