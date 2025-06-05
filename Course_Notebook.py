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
