# 1. numbers
for x in range(1,10):
	print(x)
	print(x*x)

# 2. string
for letter in "coffee":
	print(letter*10)

# 3. range
# Solution Using a Conditional
x = 0 # Store the result in x

for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

# Solution using range step
x = 0
 
for i in range(11,21,2):
        x += i


# 4. repeat
times = input("How many times do I have to tell you? ")
times = int(times)

# Simplest Version
for time in range(times):
	print("CLEAN UP YOUR ROOM")

# Version 2
for time in range(times):
	print(f"time {time+1}:CLEAN UP YOUR ROOM")


# 5. Unlucky numbers
# Main Solution
for num in range(1,21):
	if num == 4 or num == 13:
		print(f"{num} is unlucky")
	elif num % 2 == 0:
		print(f"{num} is even")
	else:
		print(f"{num} is odd")

	
# Slight Refactor
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")