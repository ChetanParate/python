a = 9
b = 8
c = sum ((a,b)) #buildin function
print(c)

def fun_calculater(num_one, num_two):
    add = num_one + num_two
    sub = num_one - num_two
    div = num_one / num_two
    mult = num_one * num_two
    return add , sub, div, mult

add_result, sub_result, div_result, mult_result = fun_calculater(20, 10)

print(add_result,sub_result,div_result,mult_result)


add_result, _, div_result, _ = fun_calculater(20, 20)
print(add_result,div_result)

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


def create_list(some_string:str, num_times:int) -> list:
    return [some_string for i in range(num_times)]

list_result = create_list("chetan", 5)
print(list_result)

list_result = create_list(4, 5)
print(list_result)


def create_student_record( name, age, major, university = "TBD", gpa=0.0):
    return{
        "name":name,
        "age":age,
        "major":major,
        "univercity":university,
        "gpa":gpa
    }

stud_one = create_student_record("Chetan", 33, "Computer Technology", "Nagpur University", 7.9)
print(stud_one)

stud_two = create_student_record(33, 7.9, "Chetan","Computer Technology", "Nagpur University")
print(stud_two)

stud_three = create_student_record(name="chetan",university="Nagpur University", age=33, major="Computer Technology", gpa=7.9)
print(stud_three)

stud_three = create_student_record(university="Nagpur University", major="Computer Technology", age=33, gpa=7.9, name="chetan")
print(stud_three)

stud_fore = create_student_record("chetan", 33, major="Computer Technology")
print(stud_fore)

stud_five = create_student_record("chetan", 33, major="Computer Technology",university="Bhopali")
print(stud_five)