import random
list=["s","w","g"]
chance=10
no_of_chance=0
computer_point=0
human_point=0

print("\t\t\t\t Snake,Water,Gun,Game\n\n")
print("s for Snake\n g for Gun\n w for Water")

#making the game using while

while( no_of_chance<chance):
    _input=input("Snake,Water,Gun")
    _random=random.choice(list)

    if (_input==_random):
        print("Both will tie and both get 0 to each\n")

        #if user enter s

    elif ( _input=="s" and _random=="w"):
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Computer win 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")
    elif (_input=="s" and _random=="g"):
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"human point is {human_point} and computer point is {computer_point}\n")

        #if user enter w

    elif (_input=="w" and _random=="s"):
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Computer win 1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")
    elif (_input=="w" and _random=="g"):
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"human point is {human_point} and computer point is {computer_point}")

        #if user enter g

    elif (_input=="g" and _random=="s"):
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Compuetr win1 point\n")
        print(f"computer point is {computer_point} and human point is {human_point}\n")
    elif (_input=="g" and _random=="w"):
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"human point is {human_point} and computer point is {computer_point}\n")
    else:
        print("You gave a wrong input\n")
        no_of_chance=no_of_chance+1
        print(f"{chance-no_of_chance} is leftout of {chance}\n")
        print("GAMEOVER")
    if computer_point==human_point:
        print("Tie")
    elif computer_point>human_point:
        print("computer win and you loose\n")
    else:
        print("you win and computer loose")
        print(f"your points is {human_point} and computer point is {computer_point}")
