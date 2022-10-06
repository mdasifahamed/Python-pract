'''
Lists in python are Same As like Arrays in Other Languages But In Python Lists can hold different types of data
Indexing in Python Start From 0.
List Can Iterated Using Loops
'''
# Declaring A Lists


rolls = [10,20,30,40,60,70,80]
print(rolls)

#Accessing Lists Element using index exp: rolls[5]

print("Accessing Lists Element using index")
print("rolls[5]"+"= "+str(rolls[5]))

#Updating Lists Element using index exp: rolls[5]

print("Updating Lists Element using index exp: rolls[5]")
rolls[5] = 90
print(rolls)
print("rolls[5]"+"= "+str(rolls[5]))

#Inserting  Element In the List Using append() function Note: append() will isnert the element at the end of list
print("Inserting  Element In the List Using append() function Note: append() will isnert the element at the end of list")
print("rolls.append(100)")
rolls.append(100)
print(rolls)

#Inserting  Element In the List alongwith index assinging using  function insert()
print("Inserting  Element In the List alongwith index assinging using  function insert()")
print("rolls.insert(8,110) Here 8 is the index Number And 110 is value which will inserted in the index 8")
rolls.insert(8,110)
print(rolls)


#Another example of insert() function is
print("Another example of insert() function is ")
print("rolls.insert(4,50) Here 8 is the index Number And 110 is value which will inserted in the index 8")
rolls.insert(4,50)
print(rolls)

#finding index position of value using index() function

print("#finding index position of value using index() function ")
print("rolls.index(80) Here 80 is the to finds its index")
print("The index of value 80 is "+ str(rolls.index(80)))

#Removing al the element of list using clear()
print("Removing al the element of list using clear()")
print("rolls.clear()")
rolls.clear()
print("Our Rolls List is Now : "+str(rolls))

#Deleting a List Using del keyword
print("del rolls")
del rolls
print("There will be a error at last last line That name 'rolls is defined cause list rolls is deleted from the line above")
print(rolls)

