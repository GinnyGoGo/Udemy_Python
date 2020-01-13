#== 1. Map ==

# Accept at least 2 arguments;
# A function and an "iterable" (just once)
# runs the lambda for each value in the iterable 
# and returns a map object which can be converted into another data structure

# Eg 1:
l = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, l))

doubles # [2, 4, 6, 8]

# Eg 2:
names = [
    {'first':'Rusty', 'last': 'Steele'}, 
    {'first':'Colt', 'last': 'Steele', }, 
    {'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

first_names # ['Rusty', 'Colt', 'Blue']

# Ex 1:
def decrement_list(l):
    return list(map(lambda n: n-1, l)) # return a list



#== 2. filter ==

# There is a lambda for each value in the iterable. (Return True or False)
# Returns filter object which can be converted into other iterables
# The object contains only the values (True) that return true to the lambda


# Eg: Pulling out evens into a new list

l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
# Pull the True values into a list
evens # [2,4]


# Ex: Removing Negatives

def remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))



## Combining filter and map ##

# Given this list of names:

names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string
# "Your instructor is " + each value in the array,
# but only if the value is less than 5 characters

list(map(lambda name: f"Your instructor is {name}",
     filter(lambda value: len(value) < 5, names)))

# ['Your instructor is Colt']


#== 3. All ==

# Return True if all elements of the iterable are truthy (or if the iterable is empty)

all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True


def is_all_strings(lst):
    return all(type(l) == str for l in lst)


#== 4. Any ==

# Return True if any element of the iterable is truthy. 
# If the iterable is empty, return False. 

any([0, 1, 2, 3]) # True

any([val for val in [1,2,3] if val > 2]) # True

any([val for val in [1,2,3] if val > 5]) # False


#== 5. Sorted ==

# Returns a new sorted list from the items in iterable
# sorted (works on anything that is iterable)

more_numbers = [6,1,8,2]
sorted(more_numbers) # [1, 2, 6, 8]
print(more_numbers) # [6, 1, 8, 2]

# ANOTHER EXAMPLE DATA SET
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
sorted(songs, key=lambda s: s['playcount'])


#== 6. max & min ==

# max (strings, dicts with same keys)

max([3,4,1,2]) # 4
max((1,2,3,4)) # 4
min('awesome') # 'a'
min({1:'a', 3:'c', 2:'b'}) # 1

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
min(len(name) for name in names) # 3

# find the longest name itself
max(names, key=lambda n:len(n)) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA



#== 7. Reversed ==

more_numbers = [6, 1, 8, 2]
print(list(reversed(more_numbers))) # [2, 8, 1, 6]

list(reversed('hello')) # 'olleh'


#== 8. len ==
# Return the length (the number of items) of an object. 
# The argument may be a sequence (such as a string, tuple, list, or range) 
# or a collection (such as a dictionary, set)

len('awesome') # 7
len((1,2,3,4)) # 4
len([1,2,3,4]) # 4
len(range(0,10) # 10

len({1,2,3,4}) # 4
len({'a':1, 'b':2, 'c':2} # 3


#== 9. Abs(), Sum(), Round() ==

# Ex: Greatest magnitude
def max_magnitude(nums):
    return max(abs(num) for num in nums)

# Ex: Sum evens
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)



#== 10. zip ==

# Make an iterator that aggregates elements from each of the iterables.

# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

# The iterator stops when the shortest input iterable is exhausted.

# Eg:
first_zip = zip([1,2,3], [4,5,6])

list(first_zip) # [(1, 4), (2, 5), (3, 6)]

dict(first_zip) # {1: 4, 2: 5, 3: 6}


# Ex : Use *args to unpack
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

list(zip(*five_by_two)) 

[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

