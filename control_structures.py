# Control structures
# Allows us to control the flow of execution of our programs

# Conditional Structures
# Allows us to execute different blocks of code depending on whether or not a certain condition is met.

# If
print("If usage")
age = 18
if age <= 3 :
    print ("You are a baby")
elif age <= 13:
    print ("You are a kid")
elif age <= 19:
    print ("You are a teenager")
else:
    print ("You are an adult")


# Loops
# Loops allows us to repeat a block of code multiple times.

# For
# The for loop is used to iterate over a sequence or any iterable object.
print("For usage")
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# While
# The while loop is used to repeat a block of code until a condition is true

print("While usage")
counter = 0

while (counter < 5):
    print(counter)
    counter+= 1

# Loop Control
# We can control flow of execution within loops

# Break
# The break statement is used to exit a loop prematurely, regardless of the condition. When a break is encountered,
# the loop stops and the flow of execution continues with the next statement outside the loop.

print("Break usage")
counter = 0

while (True):
    print(counter)
    counter += 1

    if counter == 5:
        break

# Continue
# The continue statement is used to skip the rest of the code within a loop and move to the next iteration

print("Continue usage")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Pass
# The pass statement is a null operation that does nothing. It is used as a placeholder when a statement is
# syntactically required but no action is desired.

print("Pass usage")
for i in range(5):
    pass

# Conclusion
# Control structures are powerful  tools that allow us to control the flow of execution of our programs.
# With conditional structures (if, if-else, if-elif-else) we can make decisions based on conditions.
# While with loops (for,while) we can repeat blocks of code multiple times. Additionally, the break, continue
# and pass statements provide us with additional control over the behaviour of loops.