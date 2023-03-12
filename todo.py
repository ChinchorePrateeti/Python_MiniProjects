print("Welcome to your todo User Prateeti..")

mytodo_list = []


# functions corresponding to relevent actions.
def add():
    my_string = ""
    addTask = input("enter your task- ").lower()
    my_string += addTask
    
    
    
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'a') as file:
        file.write(my_string+ ' ')
        
    #return my_string

def delete():
    deleteTask = input(" enter task to be deleted- ").lower()
    print(deleteTask)
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'r') as file:
        for lines in file.readlines():
            newToDo = lines.replace(deleteTask, "NNN")
            print(newToDo)
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'a') as file:
        file.write(newToDo)


def update():
    gatherItem = input("Enter task the you wnat to update- ").lower()
    updatedTask = input("enter the new task- ").lower()
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'r') as file:
        for lines in file.readlines():
            newToDo = lines.replace(gatherItem, updatedTask)
            print(newToDo)
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'a') as file:
        file.write(newToDo)



def view():
    with open ('/home/prateeti/Documents/vsCodefiles.taskFile.txt', 'r') as file:
        for lines in file.readlines():
            print(lines)



    
   

while True:
    lists = "\n1. Add task \n2. Delete task \n3. Quit todo \n4. Update \n5. View todo"
    print(lists)
    action = input("What action do you want to perform (Add, Update, Delete, View or Quit : ").lower()
    if action == "quit":
        break
    elif action == "add":
        add()
        #addTask = input("enter your task- ")
        #mytodo_list.append(addTask)
        
    elif action == "update":
        update()
        
    elif action == "delete":
        delete()
    
    elif action == "view":
        view()
    else:
        print("Invalid input")
        continue


