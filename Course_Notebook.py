# 100 DAYS OF CODE - PYTHON
# COURSE NOTEBOOK

# Printing:
print("Hello World!")
print("Hello\nHello\nHello") # \n adds new line
print("Hello" + " " + "Javier") # + concatenates the strings


# input() Function:
variable = input("A prompt for the user") # stores the user input in a variable


# len() function:
len(variable) # returns the length of a string


# Specific characters in strings:
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


# Flooring and Rounding:
int() # also floors the number (removes all digits after the decimal)
round(my_float) # rounds to the nearest whole number
round(my_float, 2) # rounds to 2 decimal places


# Assignemnt Operators:
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


# Random Module:
import random # imports module
random_int = random.randint(1, 10) # generates random int between 1 and 10 (inclusive)
random_float = random.random() # generates random float 0 <= n < 1
random_float = random.uniform(1, 10) # generates random float from range 1 <= n <= 10


# Lists:
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] # "Cherry"
fruits[-1] # "Pear" - Last item in list
fruits[0] = "Orange" # Modify item in list. Was "Cherry" now it's "Orange"
fruits.append("Cherry") # Adds single item at the end of the list
random_item = random.choice(fruits) # selects a random item from a list


# For Loops:
for fruit in fruits: # loops through every element in list
    print(fruit) # prints every item in fruits list
for number in range(1, 100): # loops from 1 (inc) to 100 (not inc)
    print(number)


# While Loops:
something_is_true = True
while something_is_true:
    print("This is true")
    something_is_true = False


# Functions:
def my_function(): # create a function
    print("Hello")
my_function() # call the function


# Imports:
# You can import from other modules (for example: random) or from other files in your project.
# You can import the whole module/file using "import <name_of_module>.""
# Or you can import pieces from the module/file.
# For example: "from <name_of_module> import <variable/function>"


# Functions with input:
def new_function(my_string): # create function, require an input
    print(my_string)
new_function("Hello") # call function by passing in an input
# Parameter = my_string, argument = "Hello"


# Dictionaries:
my_dictionary = {"Key 1": "Value 1", 
                 "Key 2": "Value 2",
                 "Key n": "Value n",} # Creating a dictionary.
print(my_dictionary["Key 1"]) # prints the value stored in "Key 1".
my_dictionary["Key x"] = "Value x" # Add new key/value to a dictionary.
my_dictionary = {} # creates an empty dictionary, or wipes the data of an existing one.
for key in my_dictionary: # Loop through a dictionary.
    print(key) # Print all the keys.
    print(my_dictionary[key]) # Print all the values.
# The values of a dictionary can be lists or even dictionaries.


# Functions with outputs:
def my_new_function(): # Create function.
    ''' This function does something.''' # Doctrings: adds explanation to the function.
    result = 3 * 2 # Do something.
    return result # Return what you did.
func_return = my_new_function() # Calls function and stores what the function returns into a variable.


# Scope:
# Global vs Local: 
#   Local only works inside functions. 
#   Global works outside too.
# Just be carefule were you declare variables/functions.
global my_variable # Way to call global variables to modify them inside a function.


# Constants:
PI = 3.14159 # Define constants with all capital letters to differentiate.


# Catching Exceptions:
""" You can use a try/except block in Python to catch any exceptions that might occur. 
For example if you imagine there could be a chance of user error. 
You can prevent it crashing your code by anticipating it. 
You trap the dangerous code inside a try block and use an except block to catch any potential errors. 
Then you define what should happen when that error occurs instead of simply just crashing and stopping the code."""
try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")


# Classes:
import turtle # turtle is a module included in Python
timmy = turtle.Turtle() # timmy is now an object created from the Turtle Class
# Classes are defined with Pascal Case spelling
# Atributes are variables defined in a class
my_screen = turtle.Screen()
print(my_screen.canvheight) # prints the attribute canvheight from Screen Class
# Methods are functions inside of Classes
my_screen.exitonclick() # example of a method in the Screen Class


# Creating Classes:
class Animal: # Create Class: User
    def __init__(self): # Initializer constructor
        pass # Empty for now
    def breathe(self):
        print("Inhale, exhale.")
animal_1 = Animal() # Create object from class
animal_1.id = "001" # Add attribute to object


# Class Inheritance:
# Inherits attributes and methods from an existing class.
class Fish(Animal):
    def __init__(self): # Gets all the stuff from the parent class
        super().__init__()
    def breathe(self): # adds stuff to methods from parent class
        super().breathe()
        print("Doing this underwater.")
    def swim(self): # new method
        print("Moving underwater.")


# Working with Files:
# Open File:
file = open("README.md", "r") 
text = file.read()
file.close()
# Or:
with open("README.md", "r") as file:
    text = file.read()
# Write to file:
with open("new_file.txt", "w") as file: # If new_file.txt doesn't exist, this method creates it.
    file.write(text)


# csv Module:
import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    for row in data:
        print(data) # prints the whole csv file divided in rows.


# pandas Library:
import pandas
data = pandas.read_csv("weather_data.csv")
print(data) # reads csv data and formats it into table.
# Way easier to use than the csv Module.
# Check Day 25 for more info.


# List Comprehension:
numbers = [1, 2, 3] # If you have a list
new_list = [num + 1 for num in numbers] # you can create a new list modifying the old one
# new_list = [2, 3, 4]
range_list = [num * 2 for num in range(1, 5)] # use range instead of list
# range_list = [2, 4, 6, 8]
names = ["Alex", "Beth", "Caroline", "Dave"]
short_names = [name for name in names if len(name) < 5] # Adds name to new list if the length is < 5
# short_names = ["Alex", "Beth", "Dave"]
# new_list = [new_item for item in list if test] -- syntax


# Dictionary Comprehension:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dictionary.items()}


# TKInter Library:
# Used to create GUIs.
# Refer to Days 27-29


# Try Catch Except:
try: # Something that might cause an exception
    pass
except: # Do this if there was an exception
    # Try to be specific with the exceptions.
    # Examples: FileNotFoundError, KeyError, TypeError, ValueError
    pass
else: # Do this if there were no exceptions
    pass
finally: # Do this no matter what happens
    pass
# Raising Exceptions:
# raise ValueError("This value is not valid") # you can check if the value falls within parameters.


# smtplib Module
# Way to send emails via Python.
import smtplib
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="hellopeople@gmail.com", password="12345678")
    connection.sendmail(
        from_addr="hellopeople@gmail.com", 
        to_addrs="momsemail@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )


# APIs (Application Programming Interface)
# A set of commands, functions, protocols and objects that programmers can use to create software 
# or interact with an external system.
import requests # type: ignore
response = requests.get(url="website_url_here")
print(response) # Prints the response code of the request.
response.raise_for_status() # raise error depending on the code from the response
data = response.json() # This is the real data


# Finished Day 34