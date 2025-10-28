# SETS
# A Set is a mutable and unordered data structure that allows us to store a collection of unique elements.
# Sets are enclosed in braces {} or created by using the set() function.

# Creation and basic operations
# To create a set, use braces or the set() function:

fruits = {"apple", "banana", "orange"}
numbers = set([1,2,3,4,5])

# Sets support mathematical set operations, such as: union (|), intersection (&), difference (-) and symmetric difference (^).

set1 = {1,2,3}
set2 = {3,4,5}

print("Set 1: ", set1)
print("Set 2: ", set2)

union = set1 | set2
print("The union of both sets is: ", union)

intersection = set1 & set2
print("The intersection of both sets is: ", intersection)

difference = set1 - set2
print("The difference between set1 and set2 is: ", difference)

symmetric_difference = set1 ^ set2
print("The symmetric difference is:", symmetric_difference)

# Set methods
# Sets in methods have several built-in methods to manipulate and access elements. Some common methods are:

# add(element): adds an element to the set
# remove(element): removes an element from the set, if the element does not exists it raises an error.
# discard(element): removes an element from the set if present. If the element does not exists, it does nothing.
# clear(): removes all elements from the set.

# Example:

fruits = {"apple", "banana", "orange"}

print("This is the set before doing an changes: ", fruits)

print("We add one element to the set 'pear':")
fruits.add("pear")
print(fruits)

print("We remove one element from the set 'apple'")
fruits.remove("apple")
print(fruits)

print("We discard one element from the set 'grape'")
fruits.discard("grape")
print(fruits)

print("We remove all elements from the set")
fruits.clear()
print(fruits)

# Data structures provide us with great flexibility and power to store and manipulate data in our programs. Lists are
# useful for ordered and mutable collections, tuples are ordered and immutable collections, dictionaries for storing
# key-value pairs and sets for unordered collections and unique elements.