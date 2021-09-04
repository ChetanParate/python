#print("First code of python", "second code of python", end=" ")
#print("second code of python")

var1 = "hey Chetan" #var1 str datatype
varTwo = 4  #varTwo int datatype
varThree = 36.5 #varthree float datatype
varThreeOne = "36.5" #varThreeOne str datatype
varFore = "36" #varFore str datatype
print(type(var1),type(varTwo), type(varThree))
print(varTwo+varThree)
print(var1+" varTwo")
print(int(varFore))
print(float(varThreeOne))
print(10*var1)
print(10*str(int(varFore)+float(varThreeOne)))
"""
int()
str()
float()
"""
# User Input
print("Enter the first number :")
firstNum = input() #it's string input
print("Your entered No:",firstNum)
print("Your entered No*10:",int(firstNum)*10)

#Calculator
print("Enter the first number :")
firstNum = input() #it's string input
print("Enter the second number :")
secNum = input() #it's string input
print("sum of entered No:",int(firstNum) + int(secNum))
print("multiply of entered No:",int(firstNum) * int(secNum))