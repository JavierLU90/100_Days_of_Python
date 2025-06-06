# 100 DAYS OF CODE - PYTHON
# COURSE NOTEBOOK

# Printing
print("Hello World!")
print("Hello\nHello\nHello") # \n adds new line
print("Hello" + " " + "Javier") # + concatenates the strings


# input() Function
variable = input("A prompt for the user") # stores the user input in a variable


# len() function
len(variable) # returns the length of a string


# Specific characters in strings
my_str = "Hello"
my_str[0] # "H"
my_str[1] # "e"
my_str[-1] # Last character ("o")


# Data types:
my_str = "Javier" # string = text characters
my_int = 123 # int = Whole numbers
my_float = 3.1416 # float = Numbers with decimals
my_bool = True # bool = True or false (0 or 1)
# Check data type:
type(variable)

# Convert data types:
int() # converts into int
float() # converts into float
str() # converts into string
# Not everything can be converted.


# Basic Operators:
# + : add, - : subtract, * : multiply, / : divide
# // : divide whole numbers, ** : exponents
# PEMDAS -> order of operations


# Flooring and Rounding
int() # also floors the number (removes all digits after the decimal)
round(my_float) # rounds to the nearest whole number
round(my_float, 2) # rounds to 2 decimal places


# Assignemnt Operators
# += , -= , *= , /=
# Add, subtract, multiply or divide the right of the equation to the left side 
# and assign the new value to the variable


# f-Strings:
age = 12
print(f"I am {age} years old")
# modifies print statements to work with variables.


# if / else statements:
if age > 10:
    print("Yeah!")
elif age == 10:
    print("Almost!")
else:
    print("Sorry!")
# Comparable operators: < , <= , > , >= , == , !=


# Modulo Operator %:
# Returns the remainder of a division.
remainder = 5 % 2 # remainder = 1


# Logical Operators:
# and , or , not


# Random Module
import random # imports module
random_int = random.randint(1, 10) # generates random int between 1 and 10 (inclusive)
random_float = random.random() # generates random float 0 <= n < 1
random_float = random.uniform(1, 10) # generates random float from range 1 <= n <= 10


# Lists
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] # "Cherry"
fruits[-1] # "Pear" - Last item in list
fruits[0] = "Orange" # Modify item in list. Was "Cherry" now it's "Orange"
fruits.append("Cherry") # Adds single item at the end of the list
random_item = random.choice(fruits) # selects a random item from a list


# For Loops
for fruit in fruits: # loops through every element in list
    print(fruit) # prints every item in fruits list
for number in range(1, 100): # loops from 1 (inc) to 100 (not inc)
    print(number)


# While Loops
something_is_true = True
while something_is_true:
    print("This is true")
    something_is_true = False


# Functions
def my_function(): # create a function
    print("Hello")
my_function() # call the function


# Imports
# You can import from other modules (for example: random) or from other files in your project.
# You can import the whole module/file using "import <name_of_module>.""
# Or you can import pieces from the module/file.
# For example: "from <name_of_module> import <variable/function>"