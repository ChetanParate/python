numOne = input()
numTwo = input()
try:
    print("sum", int(numOne)+int(numTwo))
except Exception as e:
    print(e)

try:
    user_input = input("Please enter an integer: ")
    result = 100 / int(user_input)
    print("Here is the result, 100 divided by the integer you input :", result)
#except ValueError:
#except ValueError as ve:
except(ValueError,ZeroDivisionError):
    print("Ooops an exception was thrown!")
except:
    print("Well this not expected")
else:
    print("Successfully excuted !....")

print("Outside the try/except block")

print(issubclass(ValueError, Exception))
print(issubclass(ZeroDivisionError, Exception))