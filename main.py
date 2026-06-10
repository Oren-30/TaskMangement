from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def main():
    tasks = []

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            for i, task in enumerate(tasks):
                print(f"{i}. {task['title']} ({'Done' if task['completed'] else 'Pending'})")

            try:
                index = int(input("Enter task index: "))
                mark_task_as_complete(tasks, index)
            except ValueError:
                print("Invalid input")  # ✅ REQUIRED FIX

        elif choice == "3":
            pending = view_pending_tasks(tasks)
            if not pending:
                print("No pending tasks.")
            else:
                for task in pending:
                    print(f"- {task['title']} (Due: {task['due_date']})")

        elif choice == "4":
            print(f"Progress: {calculate_progress(tasks):.2f}%")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()