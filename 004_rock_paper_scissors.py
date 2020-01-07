# Version 1: Basic Solution
# (It doesn't have the error-checking process.)

p1 = input("Player 1: rock, paper, or scissors ")
print("*** NO CHEATING ***\n" * 3)
p2 = input("Player 2: rock, paper, or scissors ")
 
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")



# Version 2: Computer AI
# random.randint(a,b) Return a random integer N such that a <= N <= b

from random import randint

player = input("Player, make your move: rock, paper, or scissors ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")


# Version 3: Adding a loop to play again

# more than 1 rounds game
# looping until a specific number of wins occur in one side
# set initial win-value
# plus 1 for each win
# State the winner 
# Add in a break for player

from random import randint
player_wins = 0 # set initial win-value
computer_wins = 0
winning_score = 3 #looping until a specific number of wins occur in one side

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}\n")
    print("...rock...")
    print("...paper...")
    print("...scissors...\n")

    player = input("(Enter your choice): ").lower()
    if player == "quit" or player == "q": # Add in a break for player
        break
    random_num = randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1 # plus 1 for each win
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins: # State the winner 
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else: 
    print("OH NO :( THE COMPUTER WON...")
