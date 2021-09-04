# Lambda function or anonymous function

def add(a,b):
    return a+b

minus = lambda x,y: x-y

print(minus(9,6))


def a_first(a):
    return a[1]

a =[[1,5],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)