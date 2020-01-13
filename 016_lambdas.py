# No function name; With a single line expression

# Comparision between normal function and lambda:
# Normal function:
def first_function(num):
    return num * num

print(first_function(9)) # 81

first_function.__name__ # 'first_function'

# Lambda:
first_lambda = lambda num: num * num
first_lambda(9) # 81

first_lambda.__name__ # '<lambda>'


# Exercises

# Ex 1：Cube
cube = lambda num: num ** 3

