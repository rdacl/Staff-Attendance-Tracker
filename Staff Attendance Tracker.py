#functions

#Option 6 alters comment on a specific employee on a specific date
def changeComment(searched_date, searched_employee, comment):
    i = date[searched_date]["employee"].index(searched_employee)
    date[searched_date]["comment"][i] = comment
    print(searched_employee + "'s comment changed on " + searched_date)

#Option 5 states if a specific employee worked on a specific date
def attendence(searched_date, searched_employee, record):
    i = date[searched_date]["employee"].index(searched_employee)
    date[searched_date]["attended"][i] = record
    print(searched_employee + " attendance on " + searched_date + 
          " changed to " + record)

#Option 4 deletes an employee from the specified date
def deleteEmployee(searched_date, deleted_employee):
    i = date[searched_date]["employee"].index(deleted_employee)
    del date[searched_date]["employee"][i]
    del date[searched_date]["attended"][i]
    del date[searched_date]["comment"][i]
    print(deleted_employee + " removed from " + searched_date)

#Option 3 adds an employee to the specified date
def addEmployee(searched_date, added_employee):
    date[searched_date]["employee"].append(added_employee)
    date[searched_date]["attended"].append("No")
    date[searched_date]["comment"].append("")
    print(added_employee + " added to " + searched_date)

#Option 2 deletes a date from the date dictionary
def deleteDate(deleted_Date):
    del date[deleted_Date]
    print(deleted_Date + " deleted")

#Option 1 adds a date to the date dictionary
def addDate(added_date):
    date[added_date] = {}
    date[added_date]["employee"] = []
    date[added_date]["attended"] = []
    date[added_date]["comment"] = []
    print(added_date + " added")

#sees if the date entered is in the date dictionary
def searchForDate(searched_date):
    if searched_date in date:
        return True
    return False

#sees if an employee is on a specific date
def searchForEmployee(searched_date, searched_employee):
    if searched_employee in date[searched_date]["employee"]:
        return True
    return False

#prints the dates for the user
def printDate():
    for d in date.keys():
        print(d)

#prints information about employees working on a specified date
def printEmployee(search_date):
    print(search_date + " Searched")
    i = 0
    for e in date[search_date]:
        try:
            employee = "Employee: " + date[search_date]["employee"][i] + ". "
            attented = "Attended: " + date[search_date]["attended"][i] + ". "
            comment = "Comment: " + date[search_date]["comment"][i]
            print(employee + attented + comment)
            i+=1
        except:
            pass
    

#nested dictionary
date = {
    "2026:07:14": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["Yes", "Yes", "Yes"] , 
        "comment":["", "", ""]},
    "2026:07:15": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["No", "Yes", "No"] , 
        "comment":["Family Emergency", "", "Sick"]},
    "2026:07:16": {
        "employee":["Ryan", "Phil", "Daniela"] , 
        "attended":["Yes", "No", "Yes"] , 
        "comment":["", "Holiday", ""]}
}

#menu and main loop
while True:
    #print(date["2026:07:14"]["employee"][0]) #prints Ryan
    #print(date["2026:07:14"]["employee"][2]) #prints Daniela
    #print(date["2026:07:14"]["employee"].index("Phil")) #prints 1
    #date["2026:07:14"]["employee"].append("Ade") #adds Ade to a specific dates employee list
    #print(date["2026:07:14"]["employee"])
    #del date["2026:07:14"]["employee"][-1] #deletes the last entry from a specific dates employee list
    #print(date["2026:07:14"]["employee"])
    #printDate()
    #printEmployee("2026:07:14")
    #addDate("2026:07:17")
    #printDate()
    #addEmployee("2026:07:17","Ryan")
    #addEmployee("2026:07:17","Phil")
    #printEmployee("2026:07:17")
    #deleteEmployee("2026:07:17", "Ryan")
    #attendence("2026:07:17","Phil","Yes")
    #printEmployee("2026:07:17")
    #changeComment("2026:07:17", "Phil", "Covering")
    #printEmployee("2026:07:17")
    #print(searchForDate("2026:07:17"))
    #print(searchForDate("2026:07:18"))
    #print(searchForEmployee("2026:07:17", "Phil"))
    #print(searchForEmployee("2026:07:17", "Ryan"))
    #deleteDate("2026:07:17")
    #printDate()
    print("\nThis is what you can do with your Attendance Tracker:\n")
    print("1 - Add a date to your Attendance Tracker")
    print("2 - Remove a date from your Attendance Tracker")
    print("3 - Add an employee to a date")
    print("4 - Remove an employee from a date")
    print("5 - Record if an employee attended work on a specific date")
    print("6 - Add a comment to a specific employee on a specific date")
    print("0 - Exit the Attendance Tracker program\n")
    print("Enter a number from the list above to perform an action")
    answer = input("What would you like to do? ")
    if answer == "1":
        print("Add date selected")
    elif answer == "2":
        print("Delete date selected")
    elif answer == "3":
        print("Add employee to date selected")
    elif answer == "4":
        print("Delete employee from date selected")
    elif answer == "5":
        print("Record employee attendance selected")
    elif answer == "6":
        print("Add employee comment selected")
    elif answer == "0":
        print("Program exited")
        exit()
    else:
        print("Unknown command. Please try again")
