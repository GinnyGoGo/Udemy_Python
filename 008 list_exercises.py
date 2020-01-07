# list()
# len()
# list_name.append([]) add single item
# list_name.extend([]) add more than one item (will add each to the list)
# list_name.insert(position, '')
# list_name.clear() remove all items from the list
# list_name.pop() remove the last item or a specified position item
# list_name.remove() remove the first item
# list_name.index() returns the index of the specified item in the list
# list_name.count() return the number of times x appears
# list_name.reverse() reverse the items in list. The slice [::-1] is a quick way to reverse a string
# list_name.sort()
# ' '.join(list_name) join the strings in list
# list_name[start:end:step] make new list from the old
# list[0],list[1] = list[1].list[0] swapping values for shuffling, sorting, algrithms
# the syntax [ _ for _ in _ ]
# Nested list can be used to make matricies, mazes, rows & columns for visualizations, tabulation and grouping data


# 1. Accessing all values in a list
numbers = [1,2,3,4]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

# 2. List Comprehension v.s. Looping
# List
nums = [1,2,3]
double_num = [x * 10 for x in nums] # no need to state x in adwance
print(double_num) # [2,4,6]

# Looping
nums = [1,2,3]
double_num = []

for x in nums:
    n = x * 2
    double_num.append(n) # !
print(double_num) # [2,4,6]

# 3. Conditional looping
numbers = [1,2,3,4,5]
[num * 2 if num % 2 == 0 else num / 2 for num in numbers]

with_vowels = "This is so much fun!"
' '.join(char for char in with_vowels if char not in "aeiou")
# "Ths s s mch fn!"

# 4. create a variable which contains a list with all the numbers that are divisible by 12.
answer = [val for val in range(1,101) if val % 12 == 0]

# 5. Nested lists
nest_list = [[1,2,3],[4,5,6],[7,8,9]]

for n in nest_list:
    for val in n:
        print(val)
# 1
# 2
# ...

# 6. Nested lists + repeat
[[num for num in range(1,4)] for val in range(1,4)]
# [[1,2,3],[1,2,3],[1,2,3]]