name = []
rolls = []
i = 0
while True:
    a = input("Enter Name: ")
    print("Enter Roll Number For %s : "%(a))
    b = input()
    name.append(a)
    rolls.append(b)
    if (len(name) == 5) and (len(rolls) == 5):
        break
print(name)
print(rolls)
