# Functions

# Functions are reusable blocks of code that allows us to encapsulate specific task and execute them
# when necessary. Functions help us organise our code, avoid repetition and make our programs more
# modular and easier to maintain.

# Definition and function call

# To define a function in Python, we use the def keyword followed by the function name and parenthesis.
# Optionally, we can specify parameters within the parenthesis. The functions code block is intended
# after the colon.

# To call a function, simply write the function name followed by parentheses:

def greeting():
    print("Hello World!")

greeting()  # Prints "Hello World!"

# Parameters and Arguments

# Functions can accept parameters, which are values passed to the function when it is called. Parameters
# are specified within the parentheses in the function definition.

def greeting (name):
    print(f"Hello, {name}!")

# When calling the function, we provide the corresponding arguments to the parameters

greeting("Pablo")
greeting("Mony")

# Return Values

# Functions can return values using the keyword return. The return value can be used by the code
# calling the function

# def sum(a,b):
#     return a + b

# result = sum (1,2)
# print(result)

# Anonymous Function -> Lambda

# Python allows the creation of anonymous functions or lambda functions, which are unnamed functions
# defined in a single line. They are commonly used for small and concise functions

square = lambda x: x ** 2
print(square(5)) # Prints 25

def sumar_3(number):
    return number + 3

sum_3 = lambda x: x + 3

print(sumar_3(3))
print(sum_3(3))

# Variable scope (local vs global)

# Variables defined within a function have a local scope, meaning they are only accesible within the
# function. On other hand, variables defined outside of any function have a global scope can be
# accessed from any part of the program.

def function():
    local_variable = 10
    print(local_variable) # Accesible inside of the function

global_variable = 20

def function_2():
    print(global_variable) # Accesible from anywhere

function() # Prints 10
function_2() # Prints 20
print(global_variable) # Prints 20
# print(local_variable) # Generates an error, the variable is not defined in this scope

# Function documentation (docstrings)

# It is a good practice to document our functions using docstrings. Docstrings are text strings that
# describe the purpose, parameters and return value of a function. They are placed immediately after
# the function definition and enclosed in triple double quotes.

def rectangle_area(base, height):
    """
    Calculates the area of a rectangle.

    Args:
        base (float): The base of a rectangle.
        height (float): The height of a rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return base * height

print(rectangle_area(2,6))

# Functions with variable Number of Arguments

# Python allows us to define functions that accept a variable number of arguments. This is achieved
# by using the * operator before the parameter name.

def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(variable_sum(1,2,3,4))
print(variable_sum(1,2,3,4,5,6))

def calcular_promedio(*numbers):
    suma = sum(numbers)
    cantidad = len(numbers)
    promedio = suma / cantidad
    return promedio

print(calcular_promedio(10,10))

# Functions are a fundamental tool in programming and allow us to structure and modularise our code.
# With the ability to define custom functions, we can encapsulate specific tasks and reuse them
# in different parts of our program.

# In addition to user-defined functions, Python also provides a wide range of built-in functions that
# we can use directly, such as print(), len() and range(), among others.