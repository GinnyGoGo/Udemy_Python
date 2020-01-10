# Defining Functions

def happy_birthday(): # Define the function
    print("Happy Birthday to you")

happy_birthday() # Execute the function


# Parameter

def sing_happy_birthday(name): 
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print(f"Happy Birthday to Dear {name}")
    print("Happy Birthday to You")

sing_happy_birthday("Ginny") 


# Return & Parameters

def full_name(first_name, last_name):
    return(f"Your full name is {first_name} {last_name}")


# Default Parameter

def math(a, b, fn = "add"): # Default parameter can be anything
    return fn(a, b)

math(2,3) # 5
math(2,3,"subtract") # -1


# Global

# total = 0

# def increment():
    # total += 1
    # return total

# increment() # Error!

total = 0

def increment():
    global total
    total += 1
    return total

increment() # 1


# Nonlocal

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


# Documenting Functions
# Use """ """

def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"

say_hello.__doc__ # 'A simple function that returns the string hello'


# Ex 1: Talking Animals

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?" # Or directly, return noises.get(animal, '?')

# Use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise . get() will return None  if the animal is not in the dictionary.  


# Ex 2: Counting lower letters

def single_letter_count(word,letter):
    return word.lower().count(letter.lower())


# Ex 3: Multiple letter count

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}

# Ex 4: Return the num of times the search_term appears in the list

def freq(collection, term):
    return collection.count(term)