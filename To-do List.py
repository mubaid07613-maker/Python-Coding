import json
import os
from pathlib import Path
user_input = input("Enter your File Path : ")
FILE_PATH = Path(user_input.strip('"'))
print("That file path is", FILE_PATH.resolve())
if os.path.exists(FILE_PATH):
    try:
        with open(FILE_PATH, "r") as file:
            my_tasks = json.load(file)
    except json.JSONDecodeError:
        my_tasks = []
else:
    my_tasks = [{"text": "Buy Milk", "Status": "Done"}]
recycle_bin = []
while True:
    print("Enter what you wish to do: \n1-->Add New Task\n2-->Edit Task\n3-->Delete\n4-->Recycle Bin\n5-->Display List\n6-->Exit")
    choice = int (input (" "))
    match choice:
        case 1:
            while True:
                task = input ("Enter your Task : ")
                while True:
                    status = int( input ("Whats the status of your task?\n1--> Done \n2--> Pending \n"))
                    if status == 1 or status == 2:
                        if status == 1:
                            status = "Done"
                            break
                        else:
                            status = "Pending"
                            break
                    else:
                        print("Wrong input")
                        continue
                new_task = {"text": task, "Status" : status}
                my_tasks.append(new_task)
                break
        case 2:
            for index,t in enumerate(my_tasks,1):
                print(f"{index}--> {t['text']} | [{t['Status']}]")
            task_num = int(input(f"Which task number do you want to edit : (1-{len(my_tasks)})"))
            try:
                if 1 <= task_num <= len(my_tasks):
                    Task = my_tasks[task_num - 1]
                    new_status = "Pending" if Task['Status'] == 'Done' else 'Done'
                    Task['Status'] = new_status
            except ValueError:
                print("Please enter a valid number")
        case 3:
            choice = int (input("Choose :\n1-->Delete Specific Task\n2-->Delete All Tasks\n"))
            match choice:
                case 1:
                    for index,t in enumerate(my_tasks,1):
                        print(f"{index}--> {t['text']} | [{t['Status']}]")
                    task_num = int(input(f"Which task number do you want to edit : (1-{len(my_tasks)})"))
                    try:
                        if 1 <= task_num <= len(my_tasks):
                            removed_task = my_tasks.pop(task_num - 1)
                            recycle_bin.append(removed_task)
                            print(f"The task {removed_task} has been sent to recycle bin")
                    except ValueError:
                        print("Please enter a valid number")
                case 2:
                    for task in my_tasks:
                        recycle_bin.append(task)
                    my_tasks.clear()
                    print("All your tasks have been cleared and sent to recycle bin")
        case 4:
            if not recycle_bin:
                print("Recycle Bin is Empty")
            else:
                for i,recycle in enumerate (recycle_bin,1):
                    print(f"{i}-->{recycle}")
                print("Do you want to\n1-->Retrieve Task\n2-->Empty Recycle Bin\n3-->Exit")
                option = int (input(" "))
                while True:
                    match option:
                        case 1:
                            number = int (input(f"Which task do you want to retrieve?(1 to {len(recycle_bin)} "))
                            try:
                                if 1<=number<=len(recycle_bin):
                                    retrieved_task = recycle_bin.pop(number-1)
                                    my_tasks.append(retrieved_task)
                                    print(f"The task {retrieved_task} has been added into your list")
                                else:
                                    print("You entered the wrong value")
                            except ValueError:
                                print("Wrong Value")
                            break
                        case 2:
                            recycle_bin.clear()
                            print("Recycle Bin is Empty")
                            break
                        case 3:
                            break
                        case _:
                            print("Wrong Value")      

        case 5:
            for index,t in enumerate(my_tasks,1):
                print(f"{index}. {t['text']} [{t['Status']}]")
        case 6:
            print("GoodBye!")
            break
        case _:
            print("That was an invalid input")
try:
    with open(FILE_PATH, "w") as file:
        json.dump(my_tasks, file, indent=4)
    print("Tasks saved successfully")
except Exception as e:
    print(f"Error saving file: {e}")




