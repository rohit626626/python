#Guesses the number
import random
def guessGame(a,b,actual):
    guess=int(input(f"Guess a number between {a} and {b}\n"))
    nguess=1
    while guess!=actual:
        if guess<actual:
            guess=int(input(f"Enter a bigger number: "))
            nguess +=1

        else:
            guess=int(input(f"Enter a smaller number: "))
            nguess +=1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess

if __name__ == "__main__":
    a=int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    actual1=random.randint(a,b)
    print("Player 1 turn")
    g1=guessGame(a,b,actual1)
    actual2=random.randint(a,b)
    print("Player 2 turn")
    g2=guessGame(a,b,actual2)

    if g1<g2:
        print("Player 1 won the match")

    elif g1>g2:
        print("Player 2 won the match")

    else:
        print("It a Tie")

    print(f"The number for Player 1 was {actual1} and Player 2 was {actual2}")
