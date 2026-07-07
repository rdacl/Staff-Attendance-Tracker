#functions

#nested dictionary
date = {
    "2026:07:14": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["Yes", "Yes", "Yes"] , 
        "Comment":["", "", ""]},
    "2026:07:15": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["No", "Yes", "No"] , 
        "Comment":["Family Emergency", "", "Sick"]},
    "2026:07:16": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["Yes", "No", "Yes"] , 
        "Comment":["", "Holiday", ""]}
}

#menu and main loop
while True:
    #print(date["2026:07:14"]["employee"][0]) #prints Ryan
    #print(date["2026:07:14"]["employee"][2]) #prints Daniela
    #print(date["2026:07:14"]["employee"].index("Phil")) #prints 1
    print("\nThis is what you can do with your Attendance Tracker:\n")
    print("1 - Add a date to your Attendance Tracker")
    print("2 - Remove a date from your Attendance Tracker")
    print("3 - Add an employee to a date")
    print("4 - Remove an employee from a date")
    print("0 - Exit the Attendance Tracker program\n")
    answer = input("What would you like to do? ")
    if answer == "1":
        print("Add selected")
    elif answer == "2":
        print("Delete selected")
    elif answer == "0":
        print("Program exited")
        exit()
    else:
        print("Unkown command. Please try again")
