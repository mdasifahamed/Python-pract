dict1 = {'Asif': 1250, 'Fahim': 1200, 'Rahim': 1300, 'Karim': 1450, 'Tousif': 1560, 'Jayan': 1780, 'Adnan': 1650}

name = input("Enter Employee Name: ")#first user Before loop
name = name.title()#capitalizing first letter
found = 0 #check point for inner condition insde the loop
start_again = True # switch for restarting the loop
while start_again: # to start the loop
    start_again = False # Updating for stopping the loop
    for k in dict1:
        if k == name: # Conditionc hecking with the dictionary  key and input
            found = 1 # updating the checkpoint if the data is foud
            print("The Salary of %s is " % (name), dict1[name])
    if found == 1:# condition for restating the loop after found to csearch again
        check = input("Want to Know Another One Info?\nif Yes Type 'Y' To exit Type 'N' or Press Enter: ")#check point for outer loop restart
        check = check.upper()#Capitalizing the the whole word
        found = 0 # Updating the checkpoint for data again 0 to start procees inner loop again at line 9
        if check == "Y":
            #process same as from line 3
            name2 = input("Enter Employee Name: ")
            name = name2.title() #updating the varibale agin for inner loop checking  at line 9
            start_again = True # Update switch for outer loop start outer loop at line 7
    elif found == 0: # thsi checkpoint refer to at line 5 which means data not found
        print("Data Not Found For %s"%(name))
        #same process from the line 14 for line 25 to 31
        check = input("Want to Know Another One Info?\nif Yes Type 'Y' To exit Type 'N' or Press Enter: ")
        check = check.upper()
        found = 0
        if check == "Y":
            name2 = input("Enter Employee Name: ")
            name = name2.title()
            start_again = True
    else:
        break
