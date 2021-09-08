# Snake Water Gun Game
import time
import random
print("Hello!!!\nWelcome to Snake Water Gun Game.\n\nBelow are the keywords to be used for this game:\n\nS for Snake\nW for Water\nG for Gun\n")
S="Snake"
W="Water"
G="Gun"
time.sleep(2)
player_score = 0
computer_score = 0
tie = 0
for i in range(1,10):
    computer=[S,W,G]
    comp_input=random.choice(computer)
    print("This is attempt number:", i,"\nYou still have", (10-i), "chances left!")
    play=input("Please press your input:\n")
    def p(n):
        if n=="S":
            return S
        elif n=="W":
            return W
        elif n=="G":
            return G
        else:
            print("Incorrect Input")
    player=f"{p(play.upper())}"
    print("Player Input = ", player)
    print("Computer Input = ", comp_input)
    if comp_input==player:
        print("\nYou both had same input, you had tie !")
        print("\n------------------------ T I E !------------------------")
        tie=tie+1
    elif comp_input==S and player==W:
        print("\nComputer won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ L O O S E R ------------------------")
        computer_score=computer_score+1
    elif comp_input==W and player==S:
        print("\nYou won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ W I N N E R ------------------------")
        player_score = player_score + 1
    elif comp_input==G and player==S:
        print("\nComputer won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ L O O S E R ------------------------")
        computer_score = computer_score + 1
    elif comp_input==S and player==G:
        print("\nYou won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ W I N N E R ------------------------")
        player_score = player_score + 1
    elif comp_input==G and player==W:
        print("\nYou won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ W I N N E R ------------------------")
        player_score=player_score+1
    elif comp_input==W and player==G:
        print("\nComputer won the game !\nComputer selection was: ",comp_input)
        print("\n------------------------ L O O S E R ------------------------")
        computer_score = computer_score + 1
    else:
        print("\nWrong Input, please try again")
#Score:
print("===============================================================\n****************** G A M E   O V E R ********************\n\nScore Card:\n\nYou have Scored: ", player_score,"\nComputer have Scored: ", computer_score, "\nTotal number of Tie: ", tie)
if computer_score<player_score:
    print("\n\n  ******************* Y O U   W O N   T H E   G A M E ********************")
elif computer_score>player_score:
    print("\n\n ******************* Y O U   L O O S E   T H E   G A M E ********************")
else:
    print("\n\n******** T I E **********")

















