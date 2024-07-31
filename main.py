from manage import addTask, listTasks, markCompleted, deleteTasks, renameTask

def Main():
    print("***Welcome to system***")
    print("What do you want to do?")
    while(True):
        print("1. Add a task to the to-do list")
        print("2. List all the tasks in the to-do list")
        print("3. Mark a task as completed")
        print("4. Delete the entire to-do list")
        print("5. Rename a task")
        print("6. Exit")
        print("")
        
        seleccion = input("Enter your selection: ")
        print("")

        if(seleccion == "1"):
            addTask()
        
        elif(seleccion == "2"):
            listTasks()

        elif(seleccion == "3"):
            markCompleted()

        elif(seleccion == "4"):
            deleteTasks()

        elif(seleccion == "5"):
            renameTask()

        elif(seleccion == "6"):
            print("Program finished")
            print("")
            break

        else:
            print("Incorrect selection")
            print("")

Main()