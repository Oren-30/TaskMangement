from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title")
        return False

    if not validate_task_description(description):
        print("Invalid description")
        return False

    if not validate_due_date(due_date):
        print("Invalid due date")
        return False

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")
    return True


def mark_task_as_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return True

    print("Invalid task index")
    return False


def view_pending_tasks(tasks):
    return [t for t in tasks if not t["completed"]]


def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(t["completed"] for t in tasks)
    return (completed / len(tasks)) * 100