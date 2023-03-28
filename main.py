# Code Starts

# Choice command import from random module

from random import choice

# Welcome

print("Welcome to SNAKE, WATER, GUN Game")


# Start Input with if else

def startinp():
    st = input("Start the game?(Y/N) ")

    # Start
    if st == "Y" or st == "y":
        pass

    # Exit
    elif st == "N" or st == "n":
        print("Exiting...!")
        exit()

    # Invalid Input
    else:
        print("Invalid Input!\nCheck the capitalization, spelling, etc and try again!")
        exit()


# Play Again Input

def playagain():
    playa = input("\nPlay Again(Y/N):")
    if playa == "Y" or playa == "y":
        print("\n")
        game()
    elif playa == "N" or playa == "n":
        print("Thanks for playing \nExiting...!")
    else:
        print("Invalid Input!\nExiting..!")


# Executing Start Input

startinp()

# Rules
rules = [
    "1. If you select SNAKE, you can drink water and can be killed by the gun.\n",
    "2. If you select WATER, snake can drink you you can damage the gun.\n",
    "3. If you select GUN, you can kill the snake and you can be damaged by the water.\n\n",
]
print("Read the rules before playing:")
for i in range(3):
    print(rules[i])


# Game

def game():
    # User Input

    userinp = input('Enter your input: \n"Snake" for Snake, "Water" for Water and "Gun" for Gun: ')

    # Snake, Water, Gun List

    swg = ["Snake", "Water", "Gun"]

    # Computer Input

    compinp = choice(swg)

    # Same Input = Tie

    if compinp == userinp:
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, It's a tie!")
        playagain()

    # Snake Drinks Water

    elif compinp == "Snake" and userinp == "Water":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, Computer Won!")
        playagain()

    elif compinp == "Water" and userinp == "Snake":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, You Won!")
        playagain()

    # Gun Killed Snake

    elif compinp == "Gun" and userinp == "Snake":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, Computer Won!")
        playagain()

    elif compinp == "Snake" and userinp == "Gun":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, You Won!")
        playagain()

    # Water Damaging Gun

    elif compinp == "Water" and userinp == "Gun":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, Computer Won!")
        playagain()

    elif compinp == "Gun" and userinp == "Water":
        print(f"Computer's input was {compinp}\nYour input was {userinp}\nSo, You Won!")
        playagain()

    # Invalid Input

    else:
        print("Invalid Input!\nCheck the capitalization, spelling, etc and try again!")


# Run the Game

game()

# End..!
