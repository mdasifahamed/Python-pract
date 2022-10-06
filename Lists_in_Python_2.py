rolls = [10, 20, 30, 40, 50, 60, 80, 90, 100, 110]
name = ["Ashes", "Bourno", "Cameli", "Dave", "Eline", "Finn","George", "Harry", "Isli","Jane"]

print(rolls)
print(name)

#Iterating Over The Lists Line By Line
print('Rolls are :')
for i in rolls:
    print(i)

print("\n")

print("Names are :")

for j in name:
    print(j)

print("\n")

#Prinrting Their Name And Rolls According to There Index
print("Prinrting Their Name And Rolls According to There Index")
print("Name    Rolls")

for i in range(len(name)):

    for j in range(len(rolls)):

        if i == j:
            print(name[i],'',rolls[j])

print("\n")
