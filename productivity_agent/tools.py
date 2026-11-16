import json
from pathlib import Path
from datetime import date

DATA = Path(__file__).with_name("data.json")
SAMPLE = Path(__file__).with_name("sample_data.json")


def load_data() -> dict:
    # First run creates a private local copy of the fictional sample.
    if not DATA.exists():
        DATA.write_text(SAMPLE.read_text(encoding="utf-8"), encoding="utf-8")
    return json.loads(DATA.read_text(encoding="utf-8"))


def get_tasks() -> dict:
    """Return all tasks and their priority, deadline and completion status."""
    return {"status": "success", "tasks": load_data()["tasks"]}


def get_schedule() -> dict:
    """Return the fictional schedule for the sample day, 27 November 2026."""
    return {"status": "success", "date": "2026-11-27", "schedule": load_data()["schedule"]}


def add_task(title: str, deadline: str, priority: str) -> dict:
    """Add a task to the local demo file. Deadline must be YYYY-MM-DD; priority is low, medium or high."""
    title = title.strip()
    priority = priority.strip().lower()
    try:
        if date.fromisoformat(deadline).isoformat() != deadline:
            raise ValueError()
    except ValueError:
        return {"status": "error", "message": "Use YYYY-MM-DD."}
    if not title or priority not in ("low", "medium", "high"):
        return {"status": "error", "message": "Provide a title and low, medium or high priority."}
    data = load_data()
    task = {"title": title, "deadline": deadline, "priority": priority, "completed": False}
    if any(t["title"].casefold() == title.casefold() and t["deadline"] == deadline for t in data["tasks"]):
        return {"status": "error", "message": "This task already exists."}
    data["tasks"].append(task)
    DATA.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return {"status": "success", "task": task}
