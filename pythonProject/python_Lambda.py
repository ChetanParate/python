# Lambda function or anonymous function

def add(a,b):
    return a+b

minus = lambda x,y: x-y
print(minus(9,6))
add_result = lambda x: x+1
print(add_result)

print(add_result(10))

def a_first(a):
    return a[1]

a =[[1,5],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)

print((lambda x:x*10)(33))
print((lambda x,y: x%y)(33,5))

create_stud_list = lambda *args:[name for name in args]
create_stud_record = lambda  **kwargs:{key: value for key, value in kwargs.items()}

