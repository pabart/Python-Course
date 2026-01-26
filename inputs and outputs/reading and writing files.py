"""
Docstring for inputs and outputs.reading and writing files

    Reading and writing files

    Python allows us to read and write to external files. We can open files in different modes, such as
    read ("r"), write ("w") or append ("a"), and perform read and write operations.
"""

"""
    Reading files

    To read the content of a file, we first need to open it using the open() function in read more ("r").
    Then we can read the content of the file using methods like read() or readLines().

    In this example, the file "data.txt" is opened in read mode using open(). Then, the entire content
    of the file is read using the read() method and stored in the variable content. Finally, the content
    is displayed on the screen and the file is closed using the close() method.
"""

file = open("data.txt", "r") # este codigo si funciona desde la terminal, al correrlo aqui NO
content = file.read()
print(content)
file.close()

"""
    Writing Files

    To write data to a file, we open it in write mode ("w") using the open() function. If the file does
    not exist, it will be created automatically. If the file already exists, its content will be
    overwritten.

    In this example, the file "data1.txt" is opened in write mode using open(). The, the string "Hello,
    World!" is written to the file using the write() method. Finally, the file is closed using the
    close() method.
"""

file = open("data1.txt", "w")
file.write("Esto se esta escribiendo desde el script.")
file.close()

"""
    IMPORTANT!

    It is important to always close files after using them to free up system resources.
"""

"""
    You can also use the 'with' statement to handle the opening and closing of files automatically.

    In this case the file is opened using the 'with' statement and it is automatically closed once
    the with block is exited, even if an exception occurs.
"""

with open("data1.txt", "r") as file:
    content = file.read()
    print(content)

"""
    Input and Output in Python provide us with great flexibility to interact with the user and
    manipulate external files. We can request information from the user, display results on the screen
    and read or write data to text files. Always remember to properly handle the opening and closing
    of files, and consider the possible exceptions that may occur during input/output operations.
"""