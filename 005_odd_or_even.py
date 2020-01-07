# 1. Using If condition

from random import randint
num = randint(1, 1000)
if num % 2 != 0:
    print("odd")
else:
    print("even")


# 2. Using a list Comprehension

number = [1,2,3,4,5,6]
evens = [num for num in number if num % 2 == 0]
odds = [num for num in number if num % 2 != 0]


# 3. Generating Evens Using Functions

# List comprehension
def generate_evens():
    return [x for x in range(1,50) if x % 2 == 0]

# Using a loop:
def generate_evens2():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
