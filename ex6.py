# snake water gun 
import random
lst=["s","w","g"]

chance=10
no_of_chance=0
computer_point=0
humain_point=0

print("Snake, Water, Gun Game")
print("s for snake, w for water, g for gun")

while no_of_chance<chance:
    _input=input("Snake, Water, Gun: ")
    _random=random.choice(lst)

    if _input==_random: 
        print("Tie Both 0 point to each\n")

    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"your guese {_input} and computer guese is {_random}\n")
        print("computers win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")

    elif _input=="s" and _random=="w":
        humain_point=humain_point+1
        print(f"your guese {_input} and computer guese is {_random}")
        print("Human win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")

    elif _input=="w" and _random=="s":
        computer_point=computer_point+1
        print(f"your guese {_input} and computer guese is {_random}")
        print("Computer win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")


    elif _input=="w" and _random=="g":
        humain_point=humain_point+1
        print(f"your guese {_input} and computer guese is {_random}")
        print("Human win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")

    elif _input=="g" and _random=="s":
        humain_point=humain_point+1
        print(f"your guese {_input} and computer guese is {_random}")
        print("Human win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")


    elif _input=="g" and _random=="w":
        computer_point=computer_point+1
        print(f"your guese {_input} and computer guese is {_random}")
        print("Computer win 1 point \n")
        print(f"computer_point is {computer_point} and your point is {humain_point}\n")

    else:
        print("you have wrong input")

    no_of_chance=no_of_chance+1
    print(f"{chance - no_of_chance} is left out of {chance}\n")
print("Game over")

if computer_point==humain_point:
    print("Tie")

elif computer_point>humain_point:
    print("Computer wins and you loose")

else:
    print("You wins and Computer loose")

print(f"your point is {humain_point} and computer point is {computer_point}")


