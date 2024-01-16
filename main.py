import re


class Task:
    def __init__(self, title, description, due_date, priority, status):
        self.title = title
        self.description = description

        self.due_date = None
        self.set_due_date(due_date)

        self.priority = None
        self.set_priority(priority)

        self.status = None
        self.set_status(status)

    def set_status(self, status):
        if status.lower() in ["to do", "in progress", "done"]:
            self.status = status.capitalize()
        else:
            print("You entered wrong status. We setting status to 'to do'.")
            self.status = "To do"

    def set_due_date(self, due_date):
        pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        if pattern.match(due_date):
            self.due_date = due_date
        else:
            print("You enter wrong date format")

    def set_priority(self, priority):
        if priority.lower() in ["high", "medium", "low"]:
            self.priority = priority.capitalize()
        else:
            print("You enter wrong priority, we setting priority to 'low'.")
            self.priority = "low"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority, status):
        task = Task(title, description, due_date, priority, status)
        self.tasks.append(task)
        print(self.tasks)

    def display_tasks(self):
        print("===== Tasks =====")
        for task in self.tasks:
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Due date: {task.due_date}")
            print(f"Priority: {task.priority}")
            print(f"Status: {task.status}")
            print("=================")

    def delete_task(self, title):
        task = self.find_task(title)
        if task:
            self.tasks.remove(task)
            print("Task removed!")

    def edit_task(self, title):
        task = self.find_task(title)
        if task:
            print("If you don't want change some value, leave entry space empty")
            task.title = input("Enter new title: ").strip() or task.title
            task.description = input("Enter new description: ").strip() or task.description

            due_date = input("Enter new due date: ").strip()
            task.set_due_date(due_date) if due_date else None

            priority = input("Enter new priority: ").strip()
            task.set_priority(priority) if priority else None

            status = input("Enter new status: ").strip()
            task.set_status(status) if status else None

    def find_task(self, title):
        for task in self.tasks:
            if title.lower() == task.title.lower():
                return task
        print("We don't found task with this title")
        return None

    def sort_tasks_by_priority(self, order=True):
        def key_sort_tasks(task):
            priority = {"high": 3, "medium": 2, "low": 1}
            return priority.get(task.priority.lower())

        self.tasks = sorted(self.tasks, key=key_sort_tasks, reverse=order)

    def sort_tasks_by_status(self, order=True):
        def key_sort_tasks(task):
            status = {"to do": 3, "in progress": 2, "done": 1}
            return status.get(task.status.lower())

        self.tasks = sorted(self.tasks, key=key_sort_tasks, reverse=order)


def main():
    task_manager = TaskManager()
    while True:
        print("========== Task Manager ==========")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Sorting tasks")
        print("4. Delete task")
        print("5. Edit task")
        print("6. Quit")
        menu = input()

        if menu == "1":
            title = input(f"Title: ")
            description = input(f"Description: ")
            due_date = input(f"Due date (DD-MM-YYYY): ")
            priority = input(f"Priority (high, medium, low): ")
            status = input(f"Status (to do, in progress, done): ")
            task_manager.add_task(title, description, due_date, priority, status)

        elif menu == "2":
            task_manager.display_tasks()

        elif menu == "3":
            sort = input("You wanna sort by status or priority (s / p): ")

            if sort.lower() == "s":
                sort_order = input("1. Done - To do\n2. To do - Done (default 2.)\n").lower()
                if sort_order == "1":
                    task_manager.sort_tasks_by_status(False)
                else:
                    task_manager.sort_tasks_by_status()

            if sort.lower() == "p":
                sort_order = input("1. Low - High\n2. High - Low (default 2.)\n").lower()
                if sort_order == "1":
                    task_manager.sort_tasks_by_priority(False)
                else:
                    task_manager.sort_tasks_by_priority()

        elif menu == "4":
            title = input("Enter title of task you wanna delete: ")
            task_manager.delete_task(title)

        elif menu == "5":
            title = input("Enter title of task you wanna edit: ")
            task_manager.edit_task(title)

        elif menu == "6":
            break

        else:
            print("You enter wrong number (1-5)")


if __name__ == '__main__':
    main()
