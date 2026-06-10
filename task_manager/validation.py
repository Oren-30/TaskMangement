from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        return False, "Task title cannot be empty."
    return True, None


def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        return False, "Task description cannot be empty."
    return True, None


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, None
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."