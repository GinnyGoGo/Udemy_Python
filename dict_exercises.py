# two ways of making dictionary
dict_name = dict(key = 'value') # or dict([['key1','value1],['key2','value2']])
dict_name = {'name1':'value1', 'name2':'value2'}

# Accessing individual values
dict_name['key']

# Accessing all values
dict_name.values()
dict_name.keys()
dict_name.items() # for all items

# Test whether a key is in the dict. or not
'key_name' in dict_name # answer is True or False

# dict.pop()  # delete

# dict.copy()

# dict.update() # will cover the values in the same key

# {__ : __ for __ in __}  # to iterate over keys and values using .items()


# Ex 1: Concatenation
artist = {
    "first": "Neil",
    "last": "Young",
}

# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]
# or
full_name = f"{artist['first']} {artist['last']}"

# Ex2: Common Loop
for k, v in dict_name.items():
    print(f"key is{k} and value is {v}")



# Ex3: Totaling Donations
# Use a loop to calculate the total value of donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# Version 1: Loop
total_donations = 0
 
for donation in donations.values():
 total_donations += donation

# Version 2: Sum
total_donations = sum(donation for donation in donations.values())

# Version 3: simplify
total_donations = sum(donations.values())



# Ex4: Dictionary Comprehension
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key,value in numbers.items()}

print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}


# Ex5: 
{num: num**2 for num in [1,2,3,4,5]}

# Ex6: loop
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))} 
print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

# Ex7: Conditional logic
num_list = [1,2,3,4]

{ num:("even" if num % 2 == 0 else "odd") for num in num_list }
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}



# Ex8: List to Dictionary
# Version 1: Dictionary Comprehension
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

# Version 2: dict comprehension without any references to list indexes
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

# Version 3: Using dict()
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)


# Ex9: Vowels
answer = {char:0 for char in 'aeiou'} 

# or
answer = dict.fromkeys("aeiou", 0)


# Ex10: ASCII Codes
# Use chr() on the numbers between 65 and 91:
answer = {count: chr(count) for count in range(65,91)} 
# chr() will return a string if you provide the corresponding integer ASCII code.

