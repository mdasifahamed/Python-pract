import os# Module for Deleting File
import json# Module for Converting Dictinary to Json for writing to file because dictianrya cannot be written to a file direct
stu = {}#empty dictinari for storing data
stu_list = []# lsit for holding unoq data for searching
with open("Datafinder.txt","a+") as init_file:#empty file where uique value eac record to be kept for searching and tracking
    init_file.write("")
start_main = True # Start point for Main programm through while loop
print('\n')
print("\t\t\t\t\t\t\t\t\t!!!!!!!!!!!!!!!! Simple Student Management System !!!!!!!!!!!!!!!!\t\t\t\t\t\t\t\t\t")
#main program
while start_main:
    start_main = False# Stopping The mail while loop to avoid infinte looping
    print("For Adding Data Type '1'\nFor Searching Data Type '2'\nFor Updating Data Type '3'\nTo Delete A Record Type '4'\nTo close The App Type '0' ")
    option = input("Enter choice : ")# Taking User Choice To execute operations
    #Inserting Data
    if option == '1':
        start_insert = True # start point innser while loop which will run for inserting new data based on user choice after one insert
        while start_insert:
            start_insert  = False # stoping The inner inserting while to avoiding infinite Looping
            temp_list = [] # Taking an empty tempory list which will store data from Datafinder.txt file please see line 4-6
            name = input("Enter Student Name : ").title().strip()# takig User Input and converti its first letter to capital usig tittle() and Removing Leading and trailing space of string using strip()
            roll = int(input("Enter Roll For %s : "%(name))) # User Input Roll
            department = input("Enter Department Name For %s : "%(name)) #User Department
            #Storing User iNput Stu dictinary which is declared at line 3 From Line 25 to 27 are same Operation
            stu["Name"] = name
            stu["Roll"] = roll
            stu["Department"] = department
            stu_list.append(name)# Storing The name at the List stu_list which declared at line 4 see line 4
            json_object = json.dumps(stu,indent=6)# converritng the dictinary stu to json for writing to a file
            stu.clear()# after Converting dictionary To json the Stu Dictinary will be  cleared to Empty to resue it again through loop
            #opening anad converting Datafinder file To List to search That any record has or not
            with open("Datafinder.txt","r") as file:
                line = file.read()
                line = line.split('\n')
                for items in line:
                    temp_list.append(items)
            #Filtering the name  if any file related to new insert found  then the new data will not be inserted and the data which is already hase will be shown
            if name in temp_list:
                print("Record of %s is Already Exists "%(name))
                # giving Option To The User For Further operation
                choice_start_insert = input("Want To Insert Another?\nIf Yes Type 'Y'\nTo Go To Main page Type 'M'\nTo Close The App Type Anything On The KeyBoard And press Enter\nEnter Your Choice :  ")
                choice_start_insert = choice_start_insert.upper().strip()
                if choice_start_insert == 'Y':
                    start_insert = True# this will start the programm from the Line 18
                elif choice_start_insert  == 'M':
                    print('\n')
                    start_main = True# this will start the programm from the Line 11
                else:
                    print("\nThank You For Using..........")
                    break
            # If No data is for New Insert Then the File will Be written for The New Insert.
            else:
                #Creating New file with Name of The Person Whom data will be Kept In The file
                with open("%s.txt"%(name),"w") as f:
                    f.write(json_object)
                #Also Writing The Name of The person To Datafinder file For Further Searcheng Using this File
                with open("Datafinder.txt","a") as data:# Here file mode is 'a' which meansappending Here writing is not used beacuse it overwu=ite the data when The appa will close The list will be change and past will be overwritten
                    for items in stu_list:# loping throug The stu_list referenced at line 4 and at line  28
                        data.write(items+'\n')# writing list data one by one and adding a new line for 'a' file mode
                stu_list.clear()#clearing The for avooid Duplicate Values
                #after succenful Of Data Writing User will have Option for Further Operations
                choice = input("Want To Insert Another?\nIf Yes Type 'Y'\nTo Go To Main page Type 'M'\nTo Close The App Type Anything On The KeyBoard And press Enter\nEnter Your Choice :  ")
                choice = choice.upper().strip()# making The input Full Capital Letter And Remover Space before and after the String
                if choice == 'Y':
                    start_insert = True# This start the App from line 18
                elif choice == 'M':
                    print('\n')
                    start_main = True # This start the App from line 11
                else:
                    print("\nThank You For Using..........")
                    break
    # data finding
    elif option == '2':
        start2_find = True# Starting Point For Data finding Loop
        while start2_find:
            start2_find = False # Stoping  Point For Data finding Loop to avoid infinite Looping
            list2 = []# Aother tmporaya loop as Like Referenced at line 20
            name = input("Enter The Name Of The Student To Find Data  : ").strip()
            name = name.title()
            # Same Operation from line 31
            with open("Datafinder.txt","r") as file:
                data  = file.read()
                data = data.split("\n")
                for names in data:
                    list2.append(names)
            #searching in the list2 for Macthing The Name of The Person to finds His/Her data
            if name in list2:
                with open("%s.txt"%(name),"r") as file:#Opening the file if The File Is found accorind The Name In given Thright The Programm
                    data = json.load(file)#converting The file data Dictionary
                    print('\n')
                    print("Data For %s Is shown Below "%(name))
                    print("Name : ",data["Name"]+'\n'+"Roll : ",str(data["Roll"])+'\n'+"Department : ",data["Department"])
                    print('\n')
                    #Displaying option to the App user For Further Operations
                    choice = input("\nWant to Search Again ?\nIf Yes Type 'Y'\nTo Go Main Page Type 'M'\nTo Close The App Type Anything on the KeyBoard and Press Enter\nEnter Your Choice  : ")
                    print('\n')
                    choice = choice.upper().strip()# same as line 63
                    if choice == 'Y':
                        start2_find = True #This will start the programme Fron the Line 74
                    elif choice ==  "M":
                        print('\n')
                        start_main = True #This will start the programme Fron the Line 11
                    else:
                        print("\nThank You For Using..........")
                        break
            else:
                # When Conditon will become False FroM Line 86 The Below Code will executed
                print("\nData Not Found For %s!\n"%(name))
                #Displaying option to the App user For Further Operations
                choice = input("\nWant to Search Again ?\nIf Yes Type 'Y'\nFor Back To Main Page Type 'M'\nTo Close The App Type Anything on The keyboard\nEnter Your Choice : ")
                print('\n')
                choice = choice.upper().strip()# same as line 97
                if choice == 'Y':
                    start2_find = True #This will start the programme Fron the Line 74
                elif choice == 'M':
                    print('\n')
                    start_main = True#This will start the programme Fron the Line 11

                else:
                    print("\nThank You For Using..........")
                    break
    # Data Updating
    elif option == '3':
        start_update = True# Starting Point For The Loop of Updating Block
        while start_update:
            start_update = False# Stooping Point for The Loop To avoid infinte Looping
            list2 = [] #Same as  Line 77
            name = input("Enter The Name Of The Student To Update Data: ").strip()
            name = name.title()
            # Same As FroM Line 80 and Line 31
            with open("Datafinder.txt", "r") as file:
                data = file.read()
                data = data.split("\n")
                for names in data:
                    list2.append(names)
            #Conditon Checking For Data Has or Not From To file if Become Tru then Progrme will execute from here
            if name in list2:
                with open("%s.txt"%(name),"r") as file: # Opening If the condition become True from line 137
                    data = json.load(file)# Converting the file Data To dictionary
                    fields = data.keys()# retrinving dictionary keys to dislay data to Through loop from the line 143 to 146
                    print("Data For %s! is Shown Below "%(name))
                    print("Name : ", data["Name"] + '\n' + "Roll : ", str(data["Roll"]) + '\n' + "Department : ",data["Department"])
                    print("Fields Which Can Be Updated  For %s Are : "%(name))
                    i = 0 #this Just for Showing Number Besided The field See print() below
                    for items in fields:
                        i = i+1
                        print(str(i)+": "+items)
                    #Displaying options To The app User for Further Operations
                    choice_u_field = input("Are You Sure To Update Data For %s\nIf Yes Then Type 'Y'\nTo Go to Main Page Type 'M'\nTo Find Another One To Update Type 'U'\nTo Colse The App Type Anything On Keyboard And Press Enter\nEnter YOur Choice: "%(name))
                    choice_u_field = choice_u_field.upper().strip()
                    start_field= False# this start initialyy willl be false to keep the loop of upadting fields off  at line 165
                    if choice_u_field == 'Y':
                        start_field = True# This Will start the app From the Line 165
                    elif choice_u_field == 'M':
                        start_main = True #This Will start the app From the Line 11
                    elif choice_u_field == 'U':
                        start_update = True#This Will start the app From the Line 124
                    else:
                        print("\nThank You For Using..........")
                        break

                # Starting point for inner while loop of outer updtae loop which is started ata line 124 for Chosing opting to updtae One By One
                while start_field:
                    start_field = False# Stopping Point For inner while Loop to avoid infinte lopping
                    #Displaying Optins To the user For Further operation
                    print("Fields Which Can Be Updated  For %s Are : " % (name))# this Name will Be referenceed at line 128
                    i = 0  # this Just for Showing Number Besided The field See print() below
                    for items in fields: #This feild Wil be coming fro the Line 140
                        i = i + 1
                        print(str(i) + ": " + items)
                    print("\n")
                    # Displaying Optins To the user For Further operation
                    choose_field = input("Choose Field For Updating Data by Number For Example\nFor Name Type '1'\nFor Roll Type '2'\nAnd So On ..\nEnter Your choice : ")
                    if choose_field == '1':
                        #Updating Based on user Choice
                        u_name = input('Enter Updated Name For %s : '%(name)).title().strip()
                        data["Name"] = u_name# Here The data[] is dictinary which can be referenced at line 139
                        #Converting The data dictinary ehic is opened at line 139 to Json Obeject for writng TTo teh file again
                        json_object_u = json.dumps(data,indent=6)
                        with open("%s.txt"%(name),"w") as u_file:#Opening The file for name which given form The line 128
                            u_file.write(json_object_u)#Writing The file after The update of The name Actually upadting The file
                        print("DaTa Has Been SeuccessFully Updatad")
                        # Displaying Optins To the user For Further operation
                        print("\n")
                        u_choice = input("Want to Update Another Field ?\nIf Yes Then Type 'Y'\nTo Go To Main page Type 'M'\nTo Close The App Type Anything On the Keyboard And Press Enter\nEnter Your Choice :   ")
                        u_choice = u_choice.upper()
                        if u_choice == 'Y':
                            start_field = True# this start the programme From the Line 163
                        elif u_choice == 'M':
                            print('\n')
                            start_main = True# this start the programme From the Line 11
                        else:
                            print("\nThank You For Using..........")
                            break
                    elif choose_field == '2':
                        u_roll = int(input('Enter Updated Roll No. For %s : ' %(name)))
                        data["Roll"] = u_roll
                        json_object_u = json.dumps(data, indent=6)
                        with open("%s.txt" % (name),"w") as u_file:#Opening The file for name which given form The line 128
                            u_file.write(json_object_u)#Writing The file after The update of The name Actually upadting The file
                        print("DaTa Has Been SeuccessFully Updated\n")
                        # Displaying Optins To the user For Further operation
                        u_choice = input("Want to Update Another Field ?\nIf Yes Then Type 'Y'\nFor Go To Main page Type 'M'\nTo Close The App Type Anything On the Keyboard And Press Enter\nEnter Your Choice :   ")
                        u_choice = u_choice.upper()
                        if u_choice == 'Y':
                            start_field = True# this start the programme From the Line 163
                        elif u_choice == 'M':
                            print('\n')
                            start_main = True# this start the programme From the Line 11
                        else:
                            print("\nThank You For Using..........")
                            break
                    elif choose_field == '3':
                        u_dept =input('Enter Updated Department Name For %s : ' %(name)).title()
                        data["Department"] = u_dept
                        json_object_u = json.dumps(data, indent=6)
                        with open("%s.txt" % (name),"w") as u_file:  # Opening The file for name which given form The line 128
                            u_file.write(json_object_u)#Writing The file after The update of The name Actually upadting The file
                        print("DaTa Has Been SeuccessFully Upadted\n")
                        # Displaying Optins To the user For Further operatio
                        u_choice = input("Want to Update Another Field ?\nIf Yes Then Type 'Y'\nFor Go To Main page Type 'M'\nTo Close The App Type Anything On the Keyboard And Press Enter\nEnter Your Choice :   ")
                        u_choice = u_choice.upper().strip()
                        if u_choice == 'Y':
                            start_field = True# this start the programme From the Line 163
                        elif u_choice == 'M':
                            print('\n')
                            start_main = True# this start the programme From the Line 11
                        else:
                            print("\nThank You For Using..........")
                            break
                    else:
                        print("Please Type Correctly!")
                        start_field = True#this start the programme From the Line 11
            # If The Condition of Line 137 Becomes False the Below Lines Of  Codes Will Be Executed
            else:
                print("\nData Not Found For %s!\n"%(name))
                # Displaying Optins To the user For Further operation
                choice_u = input("\nWant to Search Again For Update  ?\nIf Yes Type 'Y'\nFor Back To Main Page Type 'M'\nTo Close The App Type Anything On The Keyboard And Press Enter\nEnter Your Choice : ")
                print('\n')
                choice_u = choice_u.upper().strip()
                if choice_u == 'Y':
                    start_update = True#This will Start the app from the Line 124
                elif choice_u == 'M':
                    print('\n')
                    start_main = True #This will Start the app from the Line 11
                else:
                    print("\nThank You For Using..........")
                    break

    #delete data
    elif option == '4':
        start_delete = True # Starting point For The Loop Of Delete
        while start_delete:
            start_delete = False# Stoping poing For The Delete Loop To avoid Infinite Looping
            name = input("Enter Student Name Whose Record To Be Deleted : ").title().strip()
            name2 = name+".txt"
            # This os.path.exits is came from module os which is used for searching  the file in the same folder where The app is Located or runng from If The conditoin of line 238 become True That means a file Is presented to same name according from the line 235.
            if os.path.exists(name2):
                with open(name2,"r") as file:#Opening The the File Which name Is same to as from the Line 255
                    data = json.load(file)#Converting the file data to dictionary data
                print('\n')
                # displaying data to the user
                print("Data For %s Is Shown Below Which Will Be Deleted  " %(name))
                print("Name : ", data["Name"] + '\n' + "Roll : ", str(data["Roll"]) + '\n' + "Department : ",data["Department"])
                # Displaying Optins To the user For Further operation
                choice = input("Are You Sure To Delete Record of %s?\nIf Yes Then Type 'Y'\nTo Go To Main Page Type 'M'\nTo Close The App Type Anything Keyboard\nEnter Your Choice : "%(name))
                choice = choice.upper().strip()
                #if conditon of line 258 becomes true then the the file will be removed from the folder by os.remove() at line  272
                if choice == 'Y':
                    name2 = name + ".txt"
                    list_d = []#Temporary list same as from the line 20
                    os.remove(name2)
                    print("Record is Successfully Deleted For %s"%(name))
                    #Important opening The Datafinder file and taking its data to  list for removing The The Name whose file has been deleted from line 272 other wise it will create issue on data finding, data inserting and data updating because this datafinder file is used in sert and update and finde section to find that already the which has been searching has or not
                    with open("Datafinder.txt","r") as file2:
                        data_list = file2.read()#reading data
                        data_list = data_list.split('\n')#spilting the data
                        # Storing the data to the list which is referenced at line 271 through loop
                        for items in data_list:
                            list_d.append(items)

                    list_d.remove(name)# Removing th data which record file has been deleted
                    #After removing The Data from The List and from Datafinder file again writing The Datafinder file From The Previous State Just without the data that has deleted from line 272
                    with open("Datafinder.txt","w") as file3:
                        for names in list_d:
                            file3.write(names+'\n')
                    # Displaying Optins To the user For Further operation
                    choice_2 = input("Want To Delete Another Record ?\nIf Yes Then Type 'Y'\nTo Go Main Page Type 'M'\nTo Close The App Type Anything And Press Enter\nEnter Your Choice : ")
                    choice_2 = choice_2.upper().strip()
                    if choice_2 == 'Y':
                        start_delete = True#This Will Start The App From The Line 252
                    elif choice_2 == 'M':
                        print('\n')
                        start_main = True #This Will Start The App From The Line 11
                    else:
                        print("\nThank You For Using..........")
                        break
                elif choice == 'M':
                        print('\n')
                        start_main = True #This Will Start The App From The Line 11
                else:
                    print("\nThank You For Using..........")
                    break

            #If The Condition Of The Line 258 Become False Then next bLock of The Code Will be Executed
            else:
                print("Data Not Found For %s"%(name))
                # Displaying Optins To the user For Further operation
                choice_2 = input("Want To Delete Another Record ?\nIf Yes Then Type 'Y'\nTo Go Main Page Type 'M'\nTo Close The App Type Anything And Press Enter\nEnter Your Choice : ")
                choice_2 = choice_2.upper().strip()
                if choice_2 == 'Y':
                    start_delete = True#This Will Start The App From The Line 252
                elif choice_2 == 'M':
                    print('\n')
                    start_main = True#This Will Start The App From The Line 11
                else:
                    print("\nThank You For Using..........")
                    break
    elif option == '0':
        print("\nThank You For Using..........")
        break

    else:
        print("\t\t\t\t\t\t\t\t\t!!!!!!!!!!!!!!!! Please Type Correctly !!!!!!!!!!!!!!!!\t\t\t\t\t\t\t\t\t")
        start_main = True#This Will Start The App From The Line 11
