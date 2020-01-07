# 1. Secret Password
# Continues to ask for user input until the user types 'bananas'
msg = input("whats the secret password?")
while msg != "bananas":
	print("WRONG!")
	msg = input("whats the secret password?")
print("CORRECT!")


# 2. For loop v.s. While loop transformation
# for 
for num in range(1,11):
    print(num)

# while
num = 1 # set initial value
while num < 11:
	print(num)
	num += 1 # manually add

# 3. Emoji in loop
for num in range(1,11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

# 4. Repeat
msg = input("Say Something: ")

while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN, BROTHER!")

# while msg != "stop copying me":
# 	msg = input(f"{msg}\n")
# print("UGH FINE YOU WIN, BROTHER!")

# 5. Break
while True:
    command = input("Type 'exit' to exit: ")
    if (command == "exit"):
        break

for x in range(1, 101):
    print(x)
    if x == 3:
        break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 3: 
		print("do you even listen anymore?")
		break
		