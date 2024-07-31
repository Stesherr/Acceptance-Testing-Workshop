from task import Task

listTask = list([])


def addTask():
    name = input("Enter your task name: ")
    print("")
    print("Task successfully added")
    print("")
    task = Task(name)
    listTask.append(task)


def listTasks():     
    if (len(listTask) > 0):
        print("| Name of Task | State |")

        for i in range(0, len(listTask)):
            print(f"{i+1}. | {listTask[i].getName()} | {listTask[i].getState()} |")
        print()

    else:
        print("No pending tasks are stored")
        print()


def markCompleted():
    choose = input("Enter the number of the task you wish to mark as completed:  ")
    print("")

    try:
        value = int(choose)
        if ((value > 0) and (value <= len(listTask))):
            listTask.pop(value-1)
            print("Task successfully marked")
            print("")

        else:
            print("Invalid task number.")
            print("")

    except:
        print("You must enter a number")
        print("")


def deleteTasks():
    listTask.clear()
    print("Tasks successfully deleted")
    print("")


def renameTask():
    number = input("Enter task number to change: ")

    try:
        number = int(number)
    except:
        print("")
        print("You must enter a number")
        print("")
        return

    if ((number > 0) and (number <= len(listTask))):
        name = input("Enter a new name: ")
        print("")
        listTask[number-1].setName(name)
        print("Name changed successfully")
        print("")

    else:
        print("")
        print("Invalid task number")
        print("")
