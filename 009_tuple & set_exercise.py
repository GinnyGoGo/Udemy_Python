# Why? Tuples are faster than lists; Make your codes safer; Valid keys in a dictionary
# list using []; dictionary using {} or dict(); tuple using () or tuple(); sets using {} or set().
# Sets are unordered collection of unique values
# Cannot access items using in a set by index

# Tuple unpacking

def sum_all_values(*args):
    # there's a built in sum function - we'll see more later!
    return sum(args)

sum_all_values([1, 2, 3, 4]) # nope...
sum_all_values((1, 2, 3, 4)) # this does not work either...

sum_all_values(*[1, 2, 3, 4]) # 10
sum_all_values(*(1, 2, 3, 4)) # 10


# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)