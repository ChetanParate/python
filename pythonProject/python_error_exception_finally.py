try:
    raise Exception("green", "eggs", "and", "ham")
except Exception as exe:
    arg_1, arg_2, _, _, =exe.args
    print(arg_2, arg_1)
    print("Exception:", exe)
    print("Type:", type(exe))
    print("Arguments: ",exe.args)

def exception_raising_fn(switch):
    if switch == 1:
        raise ValueError("Value specified was wong")
    elif switch == 2:
        raise NameError("Identifier not defined in the local or global scope")
    elif switch == 3:
        #TypeError is the same as TypeError()
        raise TypeError
    else:
        print("Executed without exceptions")

try:
    exception_raising_fn(1)
except ValueError as ve:
    print("Oops a ValueError was throw!", ve)
    print("Error type", type(ve))
except NameError as ne:
    print("Oops a NameError was throw!", ne)
    print("Error type", type(ne))
except TypeError as te:
    print("Oops a TypeError was throw!", te)
    print("Error type", type(te))
finally:
    print("Finally Block executed !")
