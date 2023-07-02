#guesses number
n=18
num_of_gus=1
print("No of guesses limit is 9")
while num_of_gus<=9:
    gus_num=int(input("Enter number: "))
    if gus_num<18:
        print("you given small number, please given hight number")
    elif gus_num>18:
        print("you given height number, please given small number")
    else:
        print("you win")
        print(num_of_gus, "no of guesses win")
        break
    print(9-num_of_gus, "no of guesses left")
    num_of_gus=num_of_gus+1
if num_of_gus>9:
    print("Game over")

        

    


