import csv
import io
import json
from collections import defaultdict
from pathlib import Path

BUDGET_FILE = Path("data/processed/budget.json")


def analyze_statement(csv_text: str) -> list[str]:
    reader = csv.DictReader(io.StringIO(csv_text))
    expenses = defaultdict(float)
    total_spent = 0.0
    descriptions = defaultdict(int)

    for row in reader:
        try:
            amount = float(row.get("Amount", "0").replace(",", ""))
            category = row.get("Category", "Uncategorized")
            desc = row.get("Description", category)
        except Exception:
            continue

        expenses[category] += amount
        descriptions[desc] += 1
        total_spent += amount

    highest_category = max(expenses.items(), key=lambda x: x[1])[0]
    most_common = max(descriptions.items(), key=lambda x: x[1])[0]

    return [
        f"Total Spent: ${total_spent:.2f}",
        f"Highest Spending Category: {highest_category}",
        f"Most Recurring Expense: {most_common}",
        f"Categories: {len(expenses)} tracked",
        f"Recurring Descriptions: {len([v for v in descriptions.values() if v > 1])}",
    ]


def save_budget(amount: float):
    BUDGET_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(BUDGET_FILE, "w") as f:
        json.dump({"budget": amount}, f)


def load_budget() -> float:
    if BUDGET_FILE.exists():
        with open(BUDGET_FILE, "r") as f:
            data = json.load(f)
        return data.get("budget", 0.0)
    return 0.0
