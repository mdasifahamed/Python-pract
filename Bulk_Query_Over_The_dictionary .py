'''
Bulk Query Over The Dictionary Using dictionary  key To Get The Value Form Dictionary (key,value) Pair
'''

dict1 = {'Asif': 1250, 'Fahim': 1200, 'Rahim': 1300, 'Karim': 1450, 'Tousif': 1560, 'Jayan': 1780, 'Adnan': 1650}# main dictinary whuch will be queried
names = list() #empty list to store value gotten from the user the element of this list will be our key o to the dictionary
insert = int(input("How Many Employees Salary Info is Needed : ")) #Get number of employee name to run the loop
start = True #Switch for running the query  loop from the beginning point again


#Loop For Storing User Input To the list declared as 'name at line 6'
while insert > 0:
    name = input("Enter Names : ")# User input form consoel
    name = name.title() #Converting first letter to capital of inputed word
    names.append(name) # inserting the input valie to the list
    if len(names) == insert:#checkpoint to stop or retsrt the loop
        check = input("Do You Want Need More Names if Yes Type 'Y' Else Type 'N' : ") # check input
        check = check.upper()
        if check == 'Y':
            insert2 = int(input("How much More Names of Employess Needed: ")) # new insert of number fot restarting the loop
            insert = insert + insert2 #updating the main insert value with the input to make the loop condition will be true to run the loop at line 12
            continue # if the condition of line 19 becomes true then the loop willl run agian
        else:
            break

#Second loop for the query the name list with dictinary to get the related value
while start:#Switch to start the loop see at line 8
    start = False #Uupadting the switch to false to stop the loop if line 37 condition doest not becom true then thi updation of start will help to stop the loop
    #inner for loop to query over the dictinary based on our custom made name list at line 6
    for nam in names:
        if nam in dict1:
            print("The salary of %s  is " % (nam), dict1[nam])
        elif nam not in dict1:
            print("Data Not Found For %s " % (nam))

    check = input("Want to Bulk  Search Again ?\nIf Yes Type 'Y' or To Exit Type 'N' or Press Enter : ") # check point for running the loop again
    check = check.upper()
    if check == 'Y':
        print('\n\n')# Two line break
        #From line 40 to 55 evertinh will same as from line 11
        names = list()
        insert = int(input("How Many Employees Salary Info is Needed : "))
        while insert > 0:
            name = input("Enter Names : ")
            name = name.title()
            names.append(name)
            if len(names) == insert:
                check = input("Do You Want Need More Names if Yes Type 'Y' Else Type 'N' : ")
                check = check.upper()
                if check == 'Y':
                    insert2 = int(input("How much More Names of Employess Needed: "))
                    insert = insert + insert2
                    continue
                else:
                    break

        start = True # again update the switch start to restart the while loop as it was stoped at line 28 and this should done insde the inner condition of for loop
    else:
        break
