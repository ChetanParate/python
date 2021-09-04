i = 0
while (True):
    if i+1<5:
        i= i+1
        continue
    print(i+1, end=" ")
    if(i==20):
        break # stop the loop
    i= i+1

###############
while(1):
    inp = int(input("Enter the number:\n"))
    if inp>100:
        print("Congrats you have enter the number greater than 100 \n")
    else:
        print("Try again !")
        continue