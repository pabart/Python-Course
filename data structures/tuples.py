# TUPLES

# Tuples are immutable and ordered data structure that allows you to store a collection of elements. The elements of a tuple are enclosed in parenthesis
# (), separated by commas

# CREATION AND ACCESS

point = (1,2)

# To access the elements of a tuple, use the element's index in square brackets, just like with lists:
print(point[0])

print(point[1])

# Unlike lists, tuples are immutable which means we cannot add, edit or delete elements inside of a tuple.

# Tuples are useful when you need to store a collection of elements that should not be modified, such as coordinates or configuration data.

# TUPLES METHODS

# Altough tuples are immutable, Python provides several useful methods to work with them:

# count(element): returns the number of times an element appears inside of the tuple
# index(element): returns the position of the first ocurrence of an element in a tuple. We can even specify the start and end of the search
# len(tuple): although this is not belong to a tuple per se, this built-in functionality returns the length of a tuple

my_tuple = (1,2,3,4,5,1)

print("Times element 1 appears inside of the tuple: ", my_tuple.count(1))

print("Element 2 appears for the first time at position: ", my_tuple.index(2))

print("Element 4 appears for the first time at position: ", my_tuple.index(4,2,5))

print("my_tuple contains ", len(my_tuple), " elements")