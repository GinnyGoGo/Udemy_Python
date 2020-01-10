# The function accepts a list and a callback function (return True or False)

# Version 1: Traditional list

# Make two lists, to hold the true and false values
# Loop through the list, calling fn  with each value in the list
# If the result is True, append the value to the trues  list
# Otherwise, append the value to the falses  list
# At the end, return a list that contains both the trues and falses lists

def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]


# Version 2: List Comprehension Version

def partition2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


# Version 3:

def partition3(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]