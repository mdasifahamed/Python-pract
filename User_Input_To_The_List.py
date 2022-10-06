'''
User Input to The List using Loop

Here while loop wil be used 
indicator will be used as entry point for the starting the loop
after inserting 5 naems to the lopp indicator will be changed to False to stop The Loop

Another method can be used without using indicator variable is using  break statement  the if condition bolsck to stop the loop

'''

name = []
indicator = True
while indicator:
    a = input("Enter name : ")
    name.append(a)
    if len(name) == 5:
        indicator = False

print(name)

#Another loop
print('\n')

rolls = []

while True:
    b = input("Enter Roll :  ")
    rolls.append(b)
    if len(rolls) == 5:
        break

print(rolls)

