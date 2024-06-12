import os

class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTo-Do List Application")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self):
        task = input("Enter the task: ")
        if task:
            self.tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_completed(self):
        self.view_tasks()
        try:
            task_no = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks[task_no - 1] = f"[X] {self.tasks[task_no - 1]}"
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_completed()
            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
