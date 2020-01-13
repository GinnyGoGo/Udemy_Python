# Using min and max

# Should return a tuple containing the min and max elements.

# Call min(nums) and max(nums)
# Wrap the values I get back in a new tuple and return it!


def extremes(nums):
    return(min(nums), max(nums))

extremes([1,2,3,4,5]) # (1,5)
extremes((99,25,30,-7)) # (-7,99)
extremes('alcatraz') # ('a', 'z')


