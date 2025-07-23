# print("hello, deepseed")
# # why we use variables in programming ?
# name = "cake"

# print("i am gita, i love the name gita, was given by my fathe, paul gita, i really love the name gita ")

# print("my name is" + name + "i love the name" + name + " i was given by my father" + name + "gita")

# # Numbers
# whole_number = 42              # Integer (int)
# decimal_number = 3.14159       # Float
# complex_number = 2 + 3j        # Complex

# # Text
# greeting = "Hello, World!"     # String (str)
# single_char = 'A'             # Also a string

# # Boolean (True/False)
# is_sunny = True               # Boolean (bool)
# is_raining = False

# # Check the type of any variable
# print(type(whole_number))     # <class 'int'>
# print(type(greeting))  # <class 'str'>

# # Variable basic exmple 

# # concatinate variable  
# first nmae="emma"
# last name="rose"

# #this is not the addition > because we are not adding numbers, we are concatenating strings

# a ban name genarator

# Personal information variables
first_name = "CLOVIS"
last_name = "VIRUS"
age = 25
hobby = "coding"
city = "BAMENDA"
department = "Computer Science"
best_friend = "BIG SYSTEM FUNS"

print("My name is " + first_name + " " + last_name + ". I am " + str(age) + " years old. I love " + hobby + ", I live in " + city + ", I study in the department of " + department + ", and my best friend is " + best_friend + ".")

# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")


# Concatenation (joining strings)
first_name = "clovis"
last_name = "virus"
full_name = first_name + " " + last_name
print(full_name)  # clovis virus

# Repetition
laugh = "Ha" * 3
print(laugh)  # HaHaHa

# Length
message = "Hello, Python!"
print(len(message))  # 14

# Accessing individual characters (like opening specific drawers)
first_letter = message[0]    # H
last_letter = message[-1]    # !


# Slicing (getting a part of the string) 

name = "Alice"
age = 30
score = 95.5

# Method 1: f-strings (recommended - like fill-in-the-blank)
print(f"Hello, {name}! You are {age} years old.")
print(f"Your score is {score:.1f}%")

# Method 2: .format() method
print("Hello, {}! You are {} years old.".format(name, age))

# Method 3: % formatting (older style)
print("Hello, %s! You are %d years old." % (name, age))