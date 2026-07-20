class TaskManagerCLI:
    def __init__(self, repository):
        self.repository = repository

    def run(self):
        while True:
            print("\n===== TASK MANAGER =====")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. View Tasks by Status")
            print("4. Update Task Status")
            print("5. Delete Task")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.view_tasks_by_status()
            elif choice == "4":
                self.update_task_status()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")

    def add_task(self):
        title = input("Task title: ").strip()
        due_date = input("Due date (YYYY-MM-DD) or leave blank: ").strip() or None
        task = self.repository.add_task(title, due_date)
        print(f"Task added: {task}")

    def view_all_tasks(self):
        tasks = self.repository.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(task)

    def view_tasks_by_status(self):
        status = input("Enter status to filter (pending/done): ").strip()
        tasks = self.repository.get_tasks_by_status(status)
        if not tasks:
            print(f"No tasks with status '{status}'.")
        for task in tasks:
            print(task)

    def update_task_status(self):
        try:
            task_id = int(input("Task ID to update: ").strip())
        except ValueError:
            print("Invalid ID.")
            return
        new_status = input("New status (pending/done): ").strip()
        success = self.repository.update_task_status(task_id, new_status)
        print("Status updated." if success else "Task not found.")

    def delete_task(self):
        try:
            task_id = int(input("Task ID to delete: ").strip())
        except ValueError:
            print("Invalid ID.")
            return
        success = self.repository.delete_task(task_id)
        print("Task deleted." if success else "Task not found.")