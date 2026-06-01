import random 
choices=["rock", "scissors", "paper"]
def game():
    user=input("Choose Rock, Paper or scissors: ").lower()
    computer=random.choice(choices)
    print("Computer Chose", computer)
    if user not in choices:
        print("Invalid choice")
        return 
    if user == computer : 
        print("Its a Draw")
    elif user=="rock" and computer=="scissors":
        print("YOU WON!")
    elif user=="paper" and computer=="rock":
        print("YOU WON!")
    elif user=="scissors" and computer=="paper":
        print("YOU WON!")
    else: 
        print("you lost :(")
game()
while True:
    op=input("Do you wish to continue[Y/N]:").lower()
    if op=="y":
        game()
    else:
        print("Thank you for playing our game")
        break 
