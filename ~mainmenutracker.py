#functions

#nested dictionary

#menu and main loop
while True:
    print("\nThis is what you can do with your Attendance Tracker:\n")
    print("1 - Add an Employee to your Attendance Tracker")
    print("2 - Remove an item from your shopping list")
    print("0 - Exit the shopping list app\n")
    answer = input("What would you like to do? ")
    if answer == "1":
        print("Add selected")
    elif answer == "2":
        print("Delete selected")
    elif answer == "0":
        print("App exited")
        exit()
    else:
        print("Unkown command. Please try again")