# MAKING A TO DO LIST
user_input='random'
# CREATE A LIST FOR STORING ITEMS.
data=list()
# CREATE FOUR OPTIONS.
# 1. ADD AN ITEM
# 2. MARK AS DONE
# 3. VIEW ITEMS 
# 4. EXIT

# CREATE MENU ITEMS USING FUNCTION

def showMenu():
    print("Menu:")
    print("1. Add an item: ")
    print("2. Mark as done: ")
    print("3. View Items: ")
    print("4. Exit: ")
    

while user_input != '4':

    showMenu()
    user_input = input("Enter Your Choice:")
 
    if user_input == '1':
        item = input("What is to be done ?")
        data.append(item)
        print("Added item:",item)
    elif user_input =='2':
        item = input("What is to be marked as Done:")
        # IF ITEM IS PRESENT IN DATA
        # ELSE PRINT ITEM DOES NOT EXIST IN THE LIST
        if item in data:
            data.remove(item)
            print("Removed item:",item)
        else:
            print("Item does not exist in the to-do list")
    elif user_input == '3':
        print("List of to-do items:")
        for items in data:
            print(item)
    elif user_input =='4':
        print("Good Bye")
                


