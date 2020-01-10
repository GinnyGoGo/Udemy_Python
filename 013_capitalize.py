# Return the first letter capitalized
# capitalize("dog") -> "Dog"

def capitalize(string):
    return string[:1].upper() + string[1:]

# Slicing the first character (up to index 1) and capitalizing it
# Adding that to the rest of the string (from index 1 onward)