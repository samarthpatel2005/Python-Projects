import random
'''
1 for Stone
-1 for paper
0 for scissor
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"S": 1, "p": -1, "s": 0}
reverseDict = {1: "Stone", -1: "paper", 0: "scissor"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")