# AND OR NOT
"""
For Checking Condition with AND Both Conditions Must be True To Return result
For Checking Condition with AND At Least One Conditions Must be True To Return result
Not Checks if The condition is false or not if false then return true or if true then return false
"""
age = int(input("Enter Your Age : "))
weight = float(input("Enter Your Weight: "))


if age>=18 and weight >=68: # This condition checks if the age is greater and equla to 18 and weight must smaller or equal to 65 to be "eligible"
    print("Eligible For Next Step")
else:
    print("Not Eligible For Next Step")

print("\n")

print("Need More info ! According to your Height")

height = int(input("Enter Your Height(in Centimeter): "))
# Chaining comparision

if (age>=18 and weight>=68) or  (180<= height < 210): #any of one condition is nedded to be true for next execution
    print("Finaly  Eligible For Addmission")
else:
    print("Finaly  Not eligible for Addmission")