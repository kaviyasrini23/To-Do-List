# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

# Function to remove a task from the list
def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number you want to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

# Function to display options and handle user input
def main():
    tasks = []
    while True:
        print("\nTo-Do List Options:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
