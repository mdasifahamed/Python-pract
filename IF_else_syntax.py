#syntax of if_else

age = int(input("Enter Your age : ")) # type csteing along with input casuse input return string only and i need int value
if age <= 3:
    print("You Are an Infant")
elif age <= 8:
    print("Your Are a Child")
elif age <= 17:
    print("Your Are Not child Anymore ")
elif age <= 24:
    print("Your Are Adult Now ")
elif age <= 45:
    print("Your a Mid Age Adult ")
elif age <= 55:
    print("Your Are a Senior citizen")
else:
    print("Not eligible")
