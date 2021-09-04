a = 9
b = 8
c = sum ((a,b)) #build in function
print(c)

def functionOne():
    print("Hello you in functionOne")

def functionTwo(a,b):
    print("Hello you in functionTwo",a+b)

def functionThree(a,b):
    """this is the function which will calculate average of two number"""
    print("Hello you in functionThree")
    average = (a+b)/2
    #print(average)
    return average

functionOne()
functionTwo(5,7)
print(functionThree(5,7))
v = functionThree(5,7)
print(v)
print(functionThree.__doc__)