# two ways of making dictionary
dict_name = dict(key = 'value')
dict_name = {'name1':'value1', 'name2':'value2'}

# Accessing individual values
dict_name['key']

# Accessing all values
dict_name.values()
dict_name.keys()
dict_name.items()


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