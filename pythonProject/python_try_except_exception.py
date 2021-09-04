numOne = input()
numTwo = input()
try:
    print("sum", int(numOne)+int(numTwo))
except Exception as e:
    print(e)