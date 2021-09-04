# No of Guesses 8
# Print no of guesses left
# No of guesses he took to finish
# Game Over
n = 18
no_of_try = 1
print("No of Guesses is limited to 9 times only")
while(no_of_try <= 9):
    guess_no = int(input("Guess the Number:\n"))
    if guess_no < n:
        print("You enter the less number,Please input the greater number.\n")
    elif guess_no > n:
        print("You enter greater number,Please input the smaller number.\n")
    else:
        print("You Won.\n")
        print("You took ",no_of_try," No of guesses to finish.\n")
        break
    print(9-no_of_try,"No of guesses left..")
    no_of_try = no_of_try + 1
if(no_of_try>=9):
    print("Game Over")