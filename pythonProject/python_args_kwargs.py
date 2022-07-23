def fun_args(*args):
    print(args[0])
    for item in args:
        print(item)


def fun_argsone(ms, *list, **kwargs): #list of arguments args (*args) (**args)
    print(ms)
    for item in list:
        print(item)
    print("kwargs values ********")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
    print(kwargs)

def display(*args):
    print(args)


list = ["chetan", "Tejaswee", "SomeOne", "Shiva"]
keyvalue = {"one":"1","two":"2","three":"3","four":"4"}
ms = "master"
fun_args(*list)
print("*****************")
fun_argsone(ms)
print("*****************")
fun_argsone(ms,*list)
print("*****************")
fun_argsone(ms, *list, **keyvalue)
print("*****************")
display(list)
print("*****************")
display(*list)