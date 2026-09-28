# Python: Beginner Lesson 1

# In this lesson, we'll cover three topics:

# What is Python?

# Installing Python and running scripts

# Python syntax and indentation

# 1. What is Python?

# Introduction to Python programming

# Python is a high-level, general-purpose programming language. It is designed to be easy to read, write, and understand.

# Python is used to build many types of applications, including:

# Web development: Building websites and web applications.

# Data science: Analyzing data using Pandas and NumPy.

# Machine learning: Training computers to learn from data.

# Artificial intelligence: Developing AI applications.

# Automation: Automating repetitive tasks.

# Desktop applications: Creating software with graphical interfaces.

# Why learn Python?

# Simple and readable syntax.

# Beginner-friendly.

# Large collection of libraries.

# Cross-platform support (Linux, Windows, and macOS).

# Large community and extensive learning resources.

# Example

# Here is a simple Python program:

# print("Hello, World!")

# Output:

# Hello, World!

# The print() function displays text or other values on the screen.

# 2. Installing Python and running scripts

# Since you're using Fedora KDE Linux, Python is likely already installed on your laptop.

# Step 1: Check Python installation

# Open your terminal and run:

# python3 --version

# You should see something similar to:

# Python 3.x.x

# Your installed version may be different.

# If Python isn't installed, install it using:

# sudo dnf install python3

# To install pip, Python's package manager, run:

# sudo dnf install python3-pip
# Step 2: Open Python interactive mode

# In your terminal, enter:

# python3

# You'll see a prompt similar to:

# Python 3.x.x
# >>>

# Now you can write Python commands directly.

# For example:

# print("Hello, Inshal!")

# Output:

# Hello, Inshal!

# You can also perform calculations:

# 10 + 20

# Output:

# 30

# To exit interactive mode, type:

# exit()
# Important

# Interactive mode is useful for testing small pieces of code. For larger programs, you'll generally create Python script files.

# Step 3: Create your first Python script

# A Python script is a file containing Python code. Python files usually have the .py extension.

# Let's create your first script.

# Open the terminal and run:

# mkdir -p ~/Projects/python-learning
# cd ~/Projects/python-learning

# Create a file:

# nano hello.py

# Write the following code:

# print("Hello, World!")
# print("I am learning Python.")
# print("Python is easy to read.")

# Save the file in Nano using Ctrl + O, press Enter, and then Ctrl + X.

# Step 4: Run your Python script

# In the same directory, execute:

# python3 hello.py

# Output:

# Hello, World!
# I am learning Python.
# Python is easy to read.
# You have completed your first script!

# You have created a .py file and executed it using Python.

# You can also create and run Python files in VS Code, which you already have installed.

# 3. Python syntax and indentation

# Syntax means the rules for writing valid Python code.

# Just as English has grammar rules, Python has rules that determine how programs should be written.

# A. Python syntax

# Consider this example:

# name = "Inshal"
# age = 22

# print(name)
# print(age)

# Output:

# Inshal
# 22

# Let's understand each line.

# Code

	

# Explanation




# name = "Inshal"

	

# Stores text in a variable called name.




# age = 22

	

# Stores a number in age.




# print(name)

	

# Displays the value of name.




# print(age)

	

# Displays the value of age.

# Python is case-sensitive.

# For example:

# name = "Inshal"
# Name = "Ali"

# print(name)
# print(Name)

# Output:

# Inshal
# Ali

# name and Name are two different variables.

# B. Comments in Python

# Comments are notes written in code. Python ignores them when executing a program.

# Use # to write a single-line comment.

# # This is a comment
# print("Hello")

# Output:

# Hello

# Comments help you explain your code.

# C. Indentation in Python
# Very important

# Indentation means adding spaces at the beginning of a line.

# Python uses indentation to define blocks of code. Unlike some other programming languages, Python requires indentation instead of curly braces to define these blocks.

# For example:

# age = 20

# if age >= 18:
#     print("You are an adult.")

# Output:

# You are an adult.

# Notice that print() has four spaces before it. This means it belongs to the if block.

# Correct indentation

# The print statement is inside the if block.

# age = 20

# if age >= 18:
#     print("Adult")
# Valid Python
# Incorrect indentation
# age = 20

# if age >= 18:
# print("Adult")
# IndentationError

# The print() statement must be indented because it belongs to the if block.

# Indentation rules

# Use four spaces for each indentation level.

# Be consistent with indentation.

# Indent the code inside if, for, while, and function definitions.

# Avoid mixing tabs and spaces.

# Example with multiple indentation levels:

# age = 20

# if age >= 18:
#     print("Adult")

#     if age >= 60:
#         print("Senior citizen")

# The second if statement is inside the first if block, so it has an additional indentation level.


# Python — Lesson 2: Basics

# Today we'll cover:

# print() and input()
# Variables and naming rules
# Data types: int, float, str, bool
# 1. print()

# print() is used to display something on the screen.

# Basic example
# print("Hello, World!")

# Output:

# Hello, World!

# You can print numbers too:

# print(100)
# print(25.5)

# Output:

# 100
# 25.5
# Printing multiple values
# name = "Inshal"
# age = 22

# print(name, age)

# Output:

# Inshal 22

# You can also print text and variables together:

# name = "Inshal"
# age = 22

# print("My name is", name)
# print("My age is", age)

# Output:

# My name is Inshal
# My age is 22
# 2. input()

# input() is used to take information from the user.

# Example:

# name = input("Enter your name: ")

# print("Hello", name)

# If you enter:

# Inshal

# Output:

# Enter your name: Inshal
# Hello Inshal
# Important: input() returns a string

# Even if the user enters a number:

# age = input("Enter your age: ")

# print(age)
# print(type(age))

# If you enter 22, Python sees it as:

# 22
# <class 'str'>

# It is a string, not an integer.

# To convert it into an integer:

# age = int(input("Enter your age: "))

# print(age)
# print(type(age))

# Now:

# Enter your age: 22
# 22
# <class 'int'>

# This pattern is extremely common:

# age = int(input("Enter your age: "))
# 3. Variables

# A variable is a name that refers to a value.

# Think of it as a labeled box that stores data.

# name = "Inshal"
# age = 22

# Here:

# name → variable
# "Inshal" → value
# age → variable
# 22 → value

# You can use the variables later:

# name = "Inshal"
# age = 22

# print(name)
# print(age)

# Output:

# Inshal
# 22
# Changing a variable

# Variables can be reassigned:

# age = 22
# print(age)

# age = 23
# print(age)

# Output:

# 22
# 23
# 4. Variable naming rules

# Python has rules for variable names.

# Rule 1 — Use letters, numbers, and _

# Valid:

# name = "Inshal"
# age2 = 22
# student_name = "Inshal"
# Rule 2 — Don't start with a number

# ❌ Invalid:

# 2name = "Inshal"

# ✅ Correct:

# name2 = "Inshal"
# Rule 3 — No spaces

# ❌ Invalid:

# student name = "Inshal"

# ✅ Correct:

# student_name = "Inshal"

# Use _ instead of spaces.

# Rule 4 — Python is case-sensitive

# These are different variables:

# name = "Inshal"
# Name = "Ali"
# NAME = "Ahmed"

# Python treats all three separately.

# Rule 5 — Don't use Python keywords

# Python has reserved words such as:

# if
# else
# for
# while
# class
# def
# return
# True
# False

# You shouldn't use them as variable names.

# ❌

# class = "BSCS"

# ✅

# student_class = "BSCS"
# Recommended naming style

# Python commonly uses snake_case:

# student_name = "Inshal"
# student_age = 22
# total_marks = 850
# average_marks = 85.5

# This is much easier to read than:

# studentname = "Inshal"
# studentage = 22
# 5. Data types

# A data type tells Python what kind of data a value is.

# The four basic types we're learning are:

# Type	Meaning	Example
# int	Integer/whole number	25
# float	Decimal number	25.5
# str	Text/string	"Inshal"
# bool	True/False	True
# 6. int

# int means integer — a whole number without a decimal point.

# Examples:

# age = 22
# marks = 850
# students = 50
# temperature = -5

# Check its type:

# age = 22

# print(type(age))

# Output:

# <class 'int'>
# 7. float

# float is used for numbers containing a decimal point.

# height = 5.8
# price = 150.50
# percentage = 85.5

# Check the type:

# percentage = 85.5

# print(type(percentage))

# Output:

# <class 'float'>
# 8. str

# str means string.

# Strings contain text and are usually written inside quotes.

# name = "Inshal"
# university = "University of Agriculture Faisalabad"
# course = "BSCS"

# Both single and double quotes can be used:

# name = "Inshal"
# name = 'Inshal'

# Check the type:

# name = "Inshal"

# print(type(name))

# Output:

# <class 'str'>
# Strings can contain numbers
# age = "22"

# This is not an integer.

# It is:

# str

# Compare:

# age1 = 22
# age2 = "22"

# print(type(age1))
# print(type(age2))

# Output:

# <class 'int'>
# <class 'str'>

# This difference is very important.

# 9. bool

# bool means Boolean.

# It has only two possible values:

# True
# False

# Example:

# is_student = True
# is_graduated = False

# Check:

# is_student = True

# print(type(is_student))

# Output:

# <class 'bool'>
# Important

# True and False must start with capital letters.

# ✅

# is_student = True

# ❌

# is_student = true

# Python will not recognize lowercase true as the Boolean value.

# 10. Checking data types with type()

# Python provides the type() function.

# age = 22
# height = 5.8
# name = "Inshal"
# is_student = True

# print(type(age))
# print(type(height))
# print(type(name))
# print(type(is_student))

# Output:

# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# 11. Converting between data types

# Python allows you to convert values between compatible types.

# String → Integer
# age = "22"

# age = int(age)

# print(age)
# print(type(age))
# String → Float
# price = "150.5"

# price = float(price)

# print(price)
# print(type(price))
# Integer → String
# age = 22

# age = str(age)

# print(type(age))
# Integer → Float
# number = 10

# number = float(number)

# print(number)

# Output:

# 10.0
# 12. Combining input() with data types

# This is where everything comes together.

# Example 1 — Student information
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# percentage = float(input("Enter your percentage: "))

# print("Name:", name)
# print("Age:", age)
# print("Percentage:", percentage)

# Example:

# Enter your name: Inshal
# Enter your age: 22
# Enter your percentage: 85.5

# Name: Inshal
# Age: 22
# Percentage: 85.5


# Python — Lesson 3: Type Conversion, type() & isinstance()

# These three concepts are important because Python programs constantly work with different types of data.

# 1. What is Type Conversion?

# Type conversion means changing a value from one data type to another.

# For example:

# age = "22"

# age = int(age)

# print(age)

# Here, "22" starts as a str and is converted into an int.

# Common conversions
# Function	Converts to	Example
# int()	Integer	int("25") → 25
# float()	Float	float("25.5") → 25.5
# str()	String	str(25) → "25"
# bool()	Boolean	bool(1) → True
# 2. int()

# int() converts a value to an integer when possible.

# String → Integer
# number = "100"

# number = int(number)

# print(number)
# print(type(number))

# Output:

# 100
# <class 'int'>
# Float → Integer
# number = 10.8

# number = int(number)

# print(number)

# Output:

# 10

# ⚠️ int() does not round the number. It removes the decimal portion.

# int(9.9)   # 9
# int(9.1)   # 9
# int(-9.9)  # -9
# 3. float()

# float() converts a value to a decimal number.

# number = "25.5"

# number = float(number)

# print(number)
# print(type(number))

# Output:

# 25.5
# <class 'float'>

# You can also convert an integer:

# number = 10

# number = float(number)

# print(number)

# Output:

# 10.0
# 4. str()

# str() converts a value into text.

# age = 22

# age = str(age)

# print(age)
# print(type(age))

# Output:

# 22
# <class 'str'>

# This is useful when you need to combine numbers with strings manually.

# For example:

# age = 22

# message = "My age is " + str(age)

# print(message)

# Output:

# My age is 22

# We'll later learn f-strings, which provide a cleaner way to do this.

# 5. bool()

# bool() converts a value to either True or False.

# print(bool(1))
# print(bool(0))

# Output:

# True
# False

# Some common examples:

# print(bool("Hello"))  # True
# print(bool(""))       # False

# print(bool(100))      # True
# print(bool(0))        # False
# Important rule

# Generally:

# Empty values → False
# Non-empty/non-zero values → True

# Examples:

# bool("")       # False
# bool("Python") # True

# bool(0)        # False
# bool(10)       # True

# bool([])       # False
# bool([1, 2])   # True

# We'll study lists later.

# 6. Type Conversion with input()

# This is extremely important.

# Remember:

# input()

# normally returns a string.

# For example:

# age = input("Enter your age: ")

# print(type(age))

# If you enter:

# 22

# Python sees:

# <class 'str'>

# So if you want an integer, convert it:

# age = int(input("Enter your age: "))

# print(type(age))

# Now:

# <class 'int'>
# Example: adding two numbers

# ❌ Without conversion:

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# print(num1 + num2)

# If you enter:

# 10
# 20

# Output:

# 1020

# Why?

# Because Python is joining two strings:

# "10" + "20"

# becomes:

# "1020"
# Correct version
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(num1 + num2)

# Output:

# 30
# 7. Conversion Errors

# Not everything can be converted.

# For example:

# age = int("hello")

# This produces an error because "hello" isn't a valid integer.

# Similarly:

# float("Python")

# will produce an error.

# Even:

# int("10.5")

# doesn't work directly.

# Instead:

# int(float("10.5"))

# Output:

# 10

# Later, you'll learn how to handle conversion errors using try and except.

# 8. type()

# type() tells you the exact type/class of a value.

# Example:

# age = 22

# print(type(age))

# Output:

# <class 'int'>

# More examples:

# print(type(10))
# print(type(10.5))
# print(type("Python"))
# print(type(True))

# Output:

# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# You can also use type() directly:

# print(type(100))
# 9. Comparing Types with type()

# You can use type() to check whether something is exactly a particular type.

# age = 22

# if type(age) == int:
#     print("Age is an integer")

# Output:

# Age is an integer

# Another example:

# name = "Inshal"

# if type(name) == str:
#     print("Name is a string")
# 10. isinstance()

# isinstance() checks whether a value is an instance of a particular type or class.

# Syntax:

# isinstance(value, type)

# Example:

# age = 22

# print(isinstance(age, int))

# Output:

# True

# Another example:

# name = "Inshal"

# print(isinstance(name, str))

# Output:

# True

# And:

# height = 5.8

# print(isinstance(height, int))

# Output:

# False
# 11. type() vs isinstance()

# This difference is important.

# type()

# Checks the exact type:

# x = 10

# print(type(x) == int)

# Output:

# True
# isinstance()

# Checks whether an object belongs to a type or an inherited class relationship.

# x = 10

# print(isinstance(x, int))

# Output:

# True

# For the basic data types you're learning right now, they often give the same practical result.

# 12. Why use isinstance()?

# isinstance() is generally preferred when you're asking:

# "Is this value an integer/string/etc.?"

# For example:

# age = 22

# if isinstance(age, int):
#     print("Age is an integer")
# else:
#     print("Age is not an integer")

# This becomes especially useful later when you learn classes and inheritance.

# 13. Checking Multiple Types

# isinstance() can check multiple types at once.

# Use a tuple:

# x = 10.5

# print(isinstance(x, (int, float)))

# Output:

# True

# Because 10.5 is a float.

# Another example:

# x = "Python"

# print(isinstance(x, (int, float)))

# Output:

# False
# 14. Practical Example

# Let's combine everything.

# value = input("Enter something: ")

# print("Value:", value)
# print("Type:", type(value))

# if isinstance(value, str):
#     print("The input is a string.")

# Remember: input() always gives you a string unless you convert it.

# Now:

# value = int(input("Enter a number: "))

# print("Value:", value)
# print("Type:", type(value))

# if isinstance(value, int):
#     print("The value is an integer.")
# 15. A Useful Mental Model

# Think about this:

# age = "22"

# At this point:

# "22"
#  ↓
# str

# Then:

# age = int(age)

# Now:

# 22
#  ↓
# int

# And:

# type(age)

# asks:

# "What type is this?"

# while:

# isinstance(age, int)

# asks:

# "Is this an integer?"