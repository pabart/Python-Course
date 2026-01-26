"""
Docstring for inputs and outputs.introduction

    Inputs/Outputs

    In Python, data input and output allow us to interact with the user and manipulate files. We can
    request information from the user, display results on the screen and read or write external files.
"""

"""
    User Data Input

    To obtain information from the user during the program's execution, we can use the input() function.
    This function displays a message on the screen and waits for the user to enter a value.

    In this example, the user is asked to enter their name and age using the input() function. The values
    entered are stored in the variables name and age, respectively. Then, these variables are used to
    display a personalised greeting on the screen.
"""
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name + ", welcome!")
print(f"You are {age} years old!")

"""
    IMPORTANT!

    The input() function always returns a string. If you want to work with other data types, such as
    integers and floats, you must perform an explicit conversion using functions like int() or float().

    In this example, the user is asked to enter their age, and the entered value is convered to an
    integer using int(). Then, a conditional structure is used to check if the age is 18 or or older
    and display a corresponding message.
"""

age2 = int(input("Enter your age again please: "))

if age2 > 18:
    print("You are an adult.")
elif age2 > 12:
    print("You are a teenager.")

"""
    Data Output

    To display information on the screen, we use the print() function. This function takes one or more
    arguments and displays them in the console.

    We can use f-strings (string formatting) to embed variables directly with a text string.

    In this case, the variables are embedded within the string using curly braces '{}' and the string
    is preceded by the letter 'f' to indicate that is a f-string.
"""

newName = "Juan"
newAge = 30

print(f"Hello, my name is {newName} and I am {newAge} years old.")