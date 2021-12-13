from os import system
tasks = []


# MAIN LOOP #################################
while True:
    system("cls")
    print("MENU")
    print("1. add task")
    print("2. show tasks")
    print("3. remove task")
    print("4. change task")
    print("5. swap tasks")
    print("0.Exit")
    option = int(input(">> "))
    if option == 1:
        system("cls")
        # ADD TASKS #################################
        while True:
            new_task = input("Name your next task: ")
            if new_task == "":
                break

            if new_task not in tasks:
                tasks.append(new_task)


    if option == 2:
        system("cls")
        # PRINT TASKS ###############################
        print("\nYour tasks: ")

        for i in range(len(tasks)):
            print(i+1, " > ", tasks[i])

        input("\nHit ENTER to continue")


    if option == 3:
        system("cls")
        # EDIT A TASK ###############################
        index = int(input("Enter task position: ")) - 1
        print("Are you sure you want to remove this task? : <<", tasks[index], ">>")
        rem_task = input("\nyes/no: ")
        if rem_task == "yes":
            tasks.pop(index)
        else:
            break


    if option == 4:
        system("cls")
        # EDIT A TASK ###############################
        index = int(input("Enter task position: ")) - 1
        new_task = input("Enter new task title: ")
        tasks[index] = new_task


    if option == 5:
        system("cls")
        index_A = int(input("Enter first task position: ")) - 1
        index_B = int(input("Enter second task position: ")) - 1
        #st = tasks.pop(index_A)                                    # st - swap tasks
        #st_1 = tasks.pop(index_B-1)
        #tasks.insert(index_B, st)
        #tasks.insert(index_A, st_1)
        tasks[index_B],tasks[index_A] = tasks[index_A],tasks[index_B]



    if option == 0:
        break