"""
    Handling Exceptions

    Exception handlings allows us to capture and manage errors in a cotrolled manner using the:
    try, except and -- optionally -- finally statements.
"""

"""
    Try

    The try block contains the code that may generate an exception. If an exception occurs within the
    try block, the execution flow is transferred to the corresponding except block.

    try:
        # Code that may generate an exception
        result = 10 / 0  # Divison by zero
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero")
"""

"""
    Except

    The except block specifies the type of exception you want to capture and handle. You can multiple
    except blocks to handle different types of exceptions.

    try:
        # Code that may generate and exception
        result = 10 / 0 # Division by zero
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except ValueError:
        print("Error: Invalid value")
"""

"""
    Finally

    The finally block is optional and always executes, regardless of whether an exception has or has
    not occured. It is commonly used to perform cleanup tasks or release resources.

    try:
        # Code that may generate an exception
        file = open("file.txt", "r")
        # Perform operations with the file
    except FileNotFoundError:
        print("Error: File not found")
    finally:
        file.close() # Always close the file, even if an exception occurs.
"""