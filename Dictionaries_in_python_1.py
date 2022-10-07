'''
Dictionaries in Python Is another type of document kepping data type
it works like key:value
In The dictionaries values canbe kept against an key
dict = {'A':"ABCDEFGH", 'B': 10} Where A&B are the keys and ABCDEFGH and 10  are their values  respectively.
'''


#Simple Dictionary

dict1 =  {
            'A': "Hello", 'B':20, 'C':12.5, 'D': True
}
print(dict1)

#Accessing Dictinary Values Using Keys

print("Accessing Dictinary Values Using Keys")
print("dict['A'],dict['D']")
print(dict1['A'],'\n',dict1['D'])
print('\n')
#Updating Dictionary Element Using Keys
print("Updating Dictionary Element Keys")
print("dict['D']= False")
dict1['D'] = False
print(dict1)
print('\n')
#Creating Dictionaries Using fromkeys() Function Note: It takes two arguments one the set of keys and another list,set of values sequncely

print("Creating Dictionaries Using fromkeys() Function")
keys = {'A','B','C','D','E','F'}
value = "Labels"
print("keys = {'A','B','C','D','E','F'}")
print('value = "Labels"')
print("dict2 = dict.fromkeys(keys,value)")
dict2 = dict.fromkeys(keys,value)
print(dict2)
print('\n')



#List of Dictionaries
print("List of Dictionaries")
print("list = [dict1,dict2]")
list = [dict1,dict2]
print(list)
print('\n')

#Accessing Element Of Dictionaries Which is Inside a List Like [{'A': 'Hello', 'B': 20, 'C': 12.5, 'D': False}, {'D': 'Labels', 'E': 'Labels', 'B': 'Labels', 'F': 'Labels', 'A': 'Labels', 'C': 'Labels'}]

print("Accessing Element Of Dictionaries Which is Inside a List Like [{'A': 'Hello', 'B': 20, 'C': 12.5, 'D': False}, {'D': 'Labels', 'E': 'Labels', 'B': 'Labels', 'F': 'Labels', 'A': 'Labels', 'C': 'Labels'}]")

print("list[0]['C'] Where 0 Is The Index of Of The List Which Means firxt dictinary And 'C' is Key of Dictionary Which Value Is Wanted ")
print("The Answer Will Be",list[0]['C'])
print('\n')

#List Inside Dictionary
print("List Inside Dictionary")
dict3 = {
    'Amount': [10,30,40,60,70],
    'Weight': [781,985,984,625,878]
}
print(dict3)
print("\n")

#Accessing List Element which Is Inside A Dictionary
print("Accessing List Element which Is Inside A Dictionary")
print("dict3['Amount'][3] Where 'Amount' is the key to the list and '3' is the index of the list element to access the list elment")
print("The Dictionary 3 is ",dict3,'\n'"And The Result Of dict['Amount'][3] is ", dict3['Amount'][3])

print('\n')

#To get (Key,value) pair Of a Dictinary Use items() Function
print('To get (Key,value) pair Of a Dictinary Use items() Function ')
print("dict1.items()")
print(dict1.items())
print('\n')

#To get the Keys Of Dictionaries Usings keys() Fucntion
print("To get the Keys Of Dictionaries Usings keys() Fucntion")
print("dict1_keys = dict1.keys()")
dict1_keys = dict1.keys()
print(dict1_keys)
print('\n')

#To get the Values Of Dictionaries Usings values() Fucntion
print("To get the Keys Of Dictionaries Usings values()  Fucntion")
print("dict1_keys = dict1.values() ")
dict1_values = dict1.values()
print(dict1_values)
print('\n')
# Remove An item of The Dictionary With the key using pop() Function
print('Remove An item of The Dictionary With the key using pop() Function')
print("dict1.pop('D') Where 'D' is the key Of The Value That Will Be Deleted ")
print("Before Delete ")
print(dict1)
dict1.pop('D')
print("After delete")
print(dict1)









