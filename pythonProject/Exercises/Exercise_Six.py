#write a pattern to print below
#Input value int numbers
#Input value boolean for pattern to print
"""
if true n = 5
*
**
***
****
if false n = 4
****
***
**
*
"""
num = int(input("Enter the numbers to print :\n"))
flag = int(input("Enter the 0(false) or 1(true) :\n"))
bol = bool(flag)
if bol is True:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif bol is False:
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

print()

if bol is True:
    for i in range(0,num+1):
            print("* " * i)
if bol is False:
    for i in range(num,0,-1):
            print("* " * i)