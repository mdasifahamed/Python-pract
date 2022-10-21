'''
Files in Python mode For Files in Python Are 
"r" =  - Read - Default value. Opens a file for reading, error if the file does not exist
"w" = - Write - Opens a file for writing, creates the file if it does not exist
"a" = - Append - Opens a file for appending, creates the file if it does not exist
"x" = -Create - Creates the specified file, returns an error if the file exists
To overwite a file Use Write mode "w"
Important Note  : only One mode Can Be Used in One Time Multiple mode Cannot Be Used in a single statement 
i.E: f = open("demo.txt",'rw') This can not be used only r or can be used in a single statement.
'''
#Creating a File And Writing to it Some String Using write() method

File = open("Demo.txt","w")
File.write("This a Demo File Creation Code Snippet ")
File.close() #After operation of file It Is good practise to close it

#Reading Demo.txt Using read() Method

File2 = open("Demo.txt",'r')
content = File2.read() #The Return Value of The read() Method can be stored into varible like in contentes or it can be used directly in print like print(x.read())
print(content)
File.close()

#Appending Demo.txt Using write method  appending mode 'a'

File3 = open("Demo.txt","a")
File3.write("in Python")
File3.close()

#Reading the file again after Appending It

File4 = open("Demo.txt", "r")
content2 = File4.read()
print(content2)
File4.close()

#To Avoid  closing file  everytime after doing operation in file with statement canbe used which will automatically close the file atfe operation example below

with open("Demo.txt","a") as file:
    file.write("\n Python Is Quite Easy For Programming")#Operation to Be done On file

with open("Demo.txt","r") as file2:
    content3 = file2.read()
    print(content3)





