"""
Docstring for modules.creating our own modules

    Besides using Python's standard modules, we can also create our own modules to organise and reuse
    our code.
"""

"""
    Create and Use Custom Modules

    To create a custom module, we simply create a new Python file with the desired name and define the
    functions, classes and variables we want to include in the module. For example, we create a file
    (in the same directory in which we are running Python) called my_module.py with our functions.

    Then, we can import and use the functions defined in my_module.py in another Python file.

    In this example, the my_module.py module is imported and the greet() and calculate_sum() functions
    defined within it are used.
"""

import my_module
my_module.greet("Juan") # Prints "Hello, Juan!"
result = my_module.calculated_sum(5,3)
print(result) # Prints 8

"""
    Code Organisation in Modules

    As our programs grow in size and complexity, it is a good practice to organise into separate modules
    according to their functionality. This allows us to ensure more readable code, grouped into modules
    and easy to maintain.

    For example, we can have a module "operations.py" that contains functions related to mathematical
    operations, and another module called "utilities.py" that contains general-porpuses functions.

    Once we have our modules created, we can import them into our code.

    By organising our code into modules, we can reuse functions and maintain more structured and grouped
    code within modules.
"""

import operations
import utilities

result = operations.add(5,6)
utilities.print_message(f"La suma es: {result}")

name = utilities.get_user_name()
utilities.print_message(f"Hello, {name}!")

