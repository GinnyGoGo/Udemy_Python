# Return a list with the values that are in both iput lists.

# Solution 1: Manual Looping 

# Define an empty list that will eventually store the in common values
# Loop through one list (l1)
# For each value, check if that value is in the other list (l2)
# If it is, append the value to the in_common list
# Return in_common  after the loop ends
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common


# Solution 2: List Comprehension

def intersection2(l1, l2):
    return [val for val in l1 if val in l2]


# Solution 3: Sets Solution

# The most efficient of the three.  
# It converts the lists to sets, 
# which removes duplicate values, and then finds the intersection of them using &. 

def intersection3(list1, list2):
    return [val for val in set(list1) & set(list2)]
