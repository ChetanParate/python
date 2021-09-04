#Exercise for Faulty Calculator : for 45*3 =555, 56+9=77, 56/6=4
print("**** Faulty Calculator For Exam ****")
opeartor = input("Please enter the Operator(+,*,/) :")

numOne = int(input("Enter the first Value :"))
numTwo = int(input("Enter the second Value :"))

if opeartor == "+":
    if numOne == 56 and numTwo == 9:
        print("Result :",77)
    else:
        print("Result:", numOne+numTwo)
elif opeartor == "*":
    if numOne == 45 and numTwo == 3:
        print("Result :", 555)
    else:
        print("Result:", numOne * numTwo)
elif opeartor == "/":
    if numOne == 56 and numTwo == 6:
        print("Result :", 4)
    else:
        print("Result:",numOne/numTwo)
else:
    print("Try again ! use +, *, / operator only")