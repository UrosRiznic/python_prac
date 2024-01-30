# Python basics
"""
 Declare a variable and print the value
 Difference between f-String function and .format function 
 Uppercased variables are once that should never be changed
 Division / and // -> 
           Division with / gives float value
           Division with // gives round value, always rounded on lover (15//2 = 8)

"""
age = 30
friend_age = 33
GOLDEN_RATION = 1.61803398875
description = "{} is {} years old."

print(age)
print("My friend has", friend_age ,"years." )
print(f"My friend has {friend_age} years.")
print("My friend has {} years.".format(friend_age))
print(description.format("Bob", 25))

math_operation = 1 + 3 * 4 / 2 - 2
print(math_operation)

num1 = 5
num2 = 7
num3 = 7/5
num3 = 7//5

# User input methods
user_name = input("What is your name? ")                # Expects string
user_name_string = str(input("What is your name? "))    # Expects string
user_age = int(input("what is you age? "))              # Expects int 





