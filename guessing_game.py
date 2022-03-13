import random 
llimit = int(input("\n\n \t\t\t\t\t\t\t\t enter lower limit \t"))
ulimit = int(input("\n\n \t\t\t\t\t\t\t\t enter upper limit \t"))
tries = int(input("\n\n \t\t\t\t\t\t\t\t how much tries you set ?? \t"))

num = random.randint(llimit,ulimit)
num_2 = random.randint(llimit,ulimit)

game_over = False
game_over_2 = False
i = 1
j = 1

print(f" \n\n \t\t\t\t\t\t\t\tyou have only {tries} tries to find the number bitween {llimit , ulimit}\n\n")
print("\n\n \t\t\t\t\t\t\t\t  its player_1 \'s turn")
while game_over == False:
    if i == tries+1 :
        print(f" \n\n\n\n \t\t\t\t\t\t\t\t you are not allow to take more than {tries} tries ")
        game_over = True
        break
    guess_number = int(input(" \n \t\t\t\t\t\t\t\t guess a number \t"))

    if guess_number == num :
        print(f" \n \t\t\t\t\t\t\t\t player_1 takes {i} tries")
        game_over = True
    else:
        if guess_number > num :
            print("\n \t\t\t\t\t\t\t\t too high !!!!! please try again.  ")
        else:
            print(" \n \t\t\t\t\t\t\t\t too low !!!!! please try again.  ")

    i += 1

print("\n\n \t\t\t\t\t\t\t\t now its player_2 \'s turn")

while game_over_2 == False:
    if j == tries+1 :
        print(f" \n\n\n\n \t\t\t\t\t\t\t\t you are not allow to take more than {tries} tries ")
        game_over_2 = True
        break
    guess_number_2 = int(input(" \n \t\t\t\t\t\t\t\t guess a number \t"))

    if guess_number_2 == num_2 :
        print(f" \n \t\t\t\t\t\t\t\t player_2 takes {j} tries")
        game_over_2 = True
    else:
        if guess_number_2 > num_2 :
            print("\n \t\t\t\t\t\t\t\t too high !!!!! please try again.  ")
        else:
            print(" \n \t\t\t\t\t\t\t\t too low !!!!! please try again.  ")

    j += 1

if i<j :
    print(f" \n\n \t\t\t\t\t\t\t\t player_1 won the match by {j-i} tries")
elif j<i :
    print(f" \n\n \t\t\t\t\t\t\t\t player_2 won the match by {i-j} tries")
else :
    print(f"\n\n \t\t\t\t\t\t\t\t match draw")