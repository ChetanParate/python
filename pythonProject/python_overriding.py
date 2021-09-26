import python_Operators as op
class A:
    classvarone = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvarone ="Instance var in class A"


    def __add__(self, other):
        return self.classvarone+self.classvarone

class B(A):
    classvartwo ="I am a class variable in class B"
    
    def __init__(self):
        super(B, self).__init__()
        self.var1 = "I am inside class A's constructor"
        self.classvarone ="Instance var in class A"


a = A()
b = A()
c =a+b
print(c)

print(b.classvarone)