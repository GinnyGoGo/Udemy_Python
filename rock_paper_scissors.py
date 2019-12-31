# Version 1: Basic Solution
# (It doesn't have the error-checking process.)

p1 = input("Player 1: rock, paper, or scissors ")
print("*** NO CHEATING ***" * 3)
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

