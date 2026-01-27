"""
Docstring for modules.importing modules

    Importing and creating modules

    In Python, a module is a a file that contains definitions and functions, classes and variables that
    can be used in other programs. Importing modules allows us to access the functionality defined in
    other files and reuse code efficiently. Additionally, we can create our own modules to organise
    and modularise our code.
"""

"""
    Keep in mind

    Python comes with a comprehensive standard library of modules that provide additional
    functionalities. These modules are available without the need to install them separately.
"""

"""
    Importing modules

    To use a module in our program, we must import it using the "import" statement. We can import an
    entire module or specific functions from a module.

    In this example, the math module is imported using the "import" statement. Then, the sqrt() function
    from the math module is used to calculate the square root of 25.
"""
import math
result = math.sqrt(25)
print(f"The square root of 25 is {result}")

"""
    We can also import specific functions from a module using the syntax from module import function.

    In this case, only the sqrt() function from the math module is imported, allowing us to use it
    directly without having to precede it with the module name.
"""
from math import sqrt
result = math.sqrt(100)
print(f"The square root of 100 is {result}")

"""
    Functions and classes of standard modules

    The Python standard library offers a wide range of modules with useful functions and classes.
    Some common examples include:

    - Math

    Provides mathematical functions, such as sqrt() (square root), sin() (sine), cos() (cosine), among
    others

    - Random

    Offers functions to generate random numbers, such as random() (random value between 0 and 1) and
    randint() (random integer between a range), among others.

    - Datetime

    Allows working with dates and times, such as datetime.now() (current date and time), datetime.date()
    (date) and datetime.time() (time), among others

    These are just a few examples of the many modules available in the Python standard library. You can
    consult the official Python documentation for more information on modules and their functionalities.
"""