# DICTIONARIES
# A dictionary is a mutable and unordered data structure that allows us to store key-value pairs.
# Each element in a dictionary consists of a unique key and its corresponding value.
# Dictionaries are enclosed in curly brackets {}, and key-value pairs are separated by commas.

# Creation and access
# To create a dictionary, use curly braces and separate the keys and values with colons.

person = {"name": "Pablo", "age": 29, "city": "Aguascalientes"}

# To access the values of a dictionary, use the corresponding key in square brackets:
print(person["name"])       # Prints "Pablo"
print(person.get("age"))    # Prints 29
print(person["city"])       # Prints Aguascalientes

# You can also use the get() method to obtain the value of a key. If the key does not exist, it will return
# (None by default).

# Dictionary methods
# Dictionaries in Python have several built-in methods to manipulate and access elements. Some common methods are:

# keys(): returns a view of all the keys in the dictionary.
# values(): returns a view of all the values in the dictionary.
# items(): returns a view of all the key-value pairs in the dictionary.
# update(another-dictionary): updates the dictionary with the key-value pairs from another dictionary.

# Example:

person = {"name": "Pablo", "age": 29, "city": "Aguascalientes"}
print("These are the keys in our dictionary: ")
print(person.keys())
print()
print("These are the values in our dictionary:")
print(person.values())
print()
print("This is the whole dictionary:")
print(person.items())
print()
print("We are adding a new key-value pair: profession to our dictionary")
person.update({"profession": "Engineer"})
print(person)