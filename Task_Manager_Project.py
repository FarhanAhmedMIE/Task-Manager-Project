import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, name, deadline):
        try:
            deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d")
            task = {
                'id': len(self.tasks) + 1,
                'name': name,
                'deadline': deadline_date,
                'completed': False
            }
            self.tasks.append(task)
            print(f"Task '{name}' created successfully!")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def update_task(self, task_id, name=None, deadline=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if name:
                    task['name'] = name
                if deadline:
                    try:
                        task['deadline'] = datetime.datetime.strptime(deadline, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD.")
                        return
                print(f"Task {task_id} updated successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as complete!")
                return
        print(f"Task with ID {task_id} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nCurrent Tasks:")
        for task in self.tasks:
            status = "Complete" if task['completed'] else "Incomplete"
            print(f"ID: {task['id']}, Name: {task['name']}, Deadline: {task['deadline'].strftime('%Y-%m-%d')}, Status: {status}")

# Example usage
if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            manager.create_task(name, deadline)
        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            name = input("Enter new task name (or press Enter to skip): ")
            deadline = input("Enter new deadline (YYYY-MM-DD) (or press Enter to skip): ")
            manager.update_task(task_id, name if name else None, deadline if deadline else None)
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_task_complete(task_id)
        elif choice == "5":
            manager.list_tasks()
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")