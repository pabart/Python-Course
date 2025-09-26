# Data Structures
# Data Structures allow us to organize and store data efficiently in our programs.
# Python provides several built-in data structures, such as lists, tuples, dictionaries
# and sets, each with its own characteristics and uses.

# Lists
# A list is a mutable and ordered data structure that allows us to store a collection
# of elements. The elements of a list can be of different data types and are enclosed
# in square brackets [], separated by commas.

# Creation and access

fruits = ["apple", "banana", "orange"]

print("Printing fruits in order")
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("Printing in reverse order")
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# Lists methods
# Lists in python have several built-in methods that allow us to manipulate and modify the elements of the list.
# Some common methods are:

# append(element): adds an element to the end of the list.
# insert(index, element): adds an element at a specific position in the list.
# remove(element): removes the first occurrence of an element in the list.
# pop(index): removes and returns the element at a specific position in the list.
# sort(): sorts the elements of the list in ascending order.
# reverse(): reverses the order of the elements in the list.

print("This is the list before doing any changes", fruits)

print("Append functionality - fruits.append('pear')")
fruits.append("pear")
print(fruits)
print(fruits)

print("Insert functionality - fruits.insert(1,'grape')")
fruits.insert(1,'grape')
print(fruits)

print("Remove functionality - fruits.remove('apple')")
fruits.remove('apple')
print(fruits)

print("Pop functionality - fruits.pop(2)")
deleted_fruit = fruits.pop(2)
print(deleted_fruit)
print(fruits)

print("Sort functionality - fruits.sort()")
fruits.sort()
print(fruits)

print("Reverse functionality - fruits.reverse()")
fruits.reverse()
print(fruits)