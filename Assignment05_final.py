# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# lredinger,191105,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""   # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
objRow = {}    # A row of data to access rows in lstTable
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu ="""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """ # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile = open("ToDoList.txt")
for dicRow in objFile:
    strData = dicRow.split(',')
    dicRow = {"Task": strData[0], "Priority": strData[1]}
    lstTable.append(dicRow)
    #print(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for objRow in lstTable:
            print(objRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        newTask = 1 #flag for new dicRow needs to be created
        task = str(input("Enter a task: "))
        for objRow in lstTable:
            if objRow.get("Task") == task:
                newTask = 0 #dicRow already exists
                print(task + " is already on your list")
                break
        # if task doesnt exist, add it
        if newTask:
            priority = str(input("Enter the priority number for this task: "))
            dicRow = {"Task": task, "Priority": (priority.strip() + "\n")}
            lstTable.append(dicRow)
            print("Updated ToDo List:")
            for objRow in lstTable:
                print(objRow)

    # Step 5 - Remove a new item to the list/Table
    elif strChoice.strip() == '3':
        for objRow in lstTable:
            print(objRow)
        print()
        delTask = 0 # flag to check if usrEdit(task) exists
        usrEdit = input("Let's get your priorities straight, which task do you want to delete?: ")
        for objRow in lstTable:
            if objRow.get("Task") == usrEdit:
                delTask = 1 #dicRow exists
                lstTable.remove(objRow)
                print(usrEdit + " has been removed")
                print("Updated ToDo List: ")
                for objRow in lstTable:
                    print(objRow)
                break
        # if nothing was deleted, print msg
        if not delTask:
            print("Sorry, " + usrEdit + " is not on your To Do List")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for objRow in lstTable:
            objFile.write(objRow.get("Task") + "," + objRow.get("Priority")) #no new line added because it is on user input (priority)
        objFile.close()
        print("Your ToDo List has been saved, time to get started!")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        input("\n\nPress the enter key to exit.")
        break  # and Exit the program
