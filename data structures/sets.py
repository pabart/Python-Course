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