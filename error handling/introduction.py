"""
    Handling errors and exceptions

    When we write programs, it is common to encounter unexpected situations or errors during execution.
    Python provides a mechanism to handle these errors in a controlled manner using exception handling.
    This allows us to capture and handle specific errors without the program abruptly stopping.

    Common errors in Python

    Before diving into exception handling, let's look at some common errors you may encounter in Python.
"""

"""
    Syntax Error (SyntaxError)

    Occurs when the code does not follow Python's syntax rules, such as forgetting colons after a
    function or loop declaration.

    def my_function() # Missing colons
        print("Hello")
"""

"""
    Name Error (NameError)

    Occurs when referencing a variable or function that has not been defined.

    print(undefined_variable)
"""

"""
    Type Error (TypeError)

    Occurs when performing an operation with incompatible data types, such as trying to add a number
    to a string

    result = 5 + "10"
"""

"""
    Index Error (Index Error)

    Occurs when trying to access an index outside the valid range of a list or sequence.

    list = [1,2,3]
    print(list[3])
"""

"""
    These are just a few examples of common errors. When an error occurs, Python generates an exception
    and displays an error message that includes the type of exception and a description of the problem.
"""