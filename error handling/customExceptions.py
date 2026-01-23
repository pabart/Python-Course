"""
    Customised Exceptions

    In addition to the exceptions build into Python, you can also create your own custom exceptions.
    This is useful when you want to handle specific situations in your program.

    To create a custom exception, you will need to create a class that inherits from the base class
    Exception or one of its subclasses.
"""

def functionF():
    # Code that may raise a custom exception
    if 1==1:
        raise Exception("Error description")

try:
    functionF()
except Exception as e:
    print(f"Error: {str(e)}")

"""
    In the previous example, a function called functionF() is defined. Inside the function, a condition
    is checked and, if met, an exception is raised using the raise statement. Instead of creating a
    custom class, the base class Exception is directly used to raise the exception.
    
    Then a try-except block is used to catch and handle the exception. The variable e is used to access
    the error description provided when the exception is raised.

    Error and exception handling is a fundamental part of programming in python. It allows you to handle
    unexpected situations in a controlled manner and prevent your program from crashing or stopping
    abruptly.

    When an error occurs in your code, Python raises an exception. By using try-except blocks, you can
    catch and handle these exceptions appropiately. You can specify different blocks to handle different
    types of exceptions and perform specific actions in each case.

    Additionally, the finally block allows you to execute cleanup or resource-release code, regardless of
    wheter or not an exception has occured. This is useful to ensure that certain actions are always
    performed, such as closing files or database connections. 
"""

"""
    IMPORTANT!

    Consider the possible erros that may occur in your code and use appropiate exception handling to
    manage them properly. They will make your programs more reliable and robust.
"""