with open("tasks.txt", "a") as file:
    file.write("program started\n")

tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(task,"added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

            delete_task = int(input("Enter task number to delete: "))
            if 1 <= delete_task <= len(tasks):
                tasks.pop(delete_task - 1)
                print("Task deleted!")
            else:
                print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")