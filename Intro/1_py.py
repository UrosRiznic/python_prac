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


#Boolean values
age = 20
is_over_age = age >= 18 # True
is_under_age = age < 18 # False 
is_twenty = age == 20   # True

num = 15
test = num > 20 and num < 20 or num >= 15   # False and True or True = True

bool(0) # False, int o
bool(13) # True, int 13
bool("") # False, string
bool("Hello") # True, string
bool([]) # False, list
bool([1,3,5]) # True, List

# and, &, or 
age = 25
result = age > 15 and age < 65 # True and True = True 
result = age > 15 and age > 65 # True and False = False 
result = age < 15 and age < 65 # False and True = False
result = age < 15 and age > 65 # False and False = False

result = age > 15 or age < 65 # True and True = True
result = age > 15 or age > 65 # True and False = True
result = age < 15 or age < 65 # False and True = True
result = age < 15 or age > 65 # False and False = False

result = age > 15 & age < 65 # True and True = True 
result = age > 15 & age > 65 # True and False = False
result = age < 15 & age < 65 # False and True = False
result = age < 15 & age > 65 # False and False = True

# LISTS
#             0       1       2
friends = ["Marko", "John", "Bob"]
random_list = ["1", "", 0, True, False]


