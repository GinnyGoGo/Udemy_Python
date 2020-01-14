#== Raise Our Own Error ==

# Raise

def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Printed {text} in {color}")

colorize([], 'cyan')
# colorize(34, "red")


#== Try and Except ==

# try
# Except

# Ex 1:

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]

# Ex 2: Division 
def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total


# Else
# Finally

while True: # repeat the entire thing
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break # stop and break out
	finally: # runs no matter what
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")


#== pdb ==
# (python debugging)

# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


# Be careful with variable names!
def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace() 

    return a + b + c + d
add_numbers(1,2,3,4)

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)