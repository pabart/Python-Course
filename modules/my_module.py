def greet(name):
    print(f"Hello, {name}!")

def calculated_sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum