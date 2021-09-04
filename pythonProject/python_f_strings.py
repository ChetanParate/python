import math

me = "chetan"
str = "This is me %s"%me
ast = 7
print(str)

strone = "This is me %s %s"%(me,ast)
print(strone)

a = "This is {} {}"
b = a.format(me, ast)
print(b)

aone = f"This is {me} {ast} {7*7}"
atwo = f"This is {me} {ast} {math.cos(65)}"
print(aone)
print(atwo)