# odd or even
from random import randint
num = randint(1, 1000)
if num % 2 != 0:
    print("odd")
else:
    print("even")

# list
number = [1,2,3,4,5,6]
evens = [num for num in number if num % 2 == 0]
odds = [num for num in number if num % 2 != 0]