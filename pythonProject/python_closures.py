def add_employee_to_department(department_name):
    employee_list = []
    def add_employee(employee_name):
        employee_list.append(employee_name)

        print(f"Added {employee_name} to {department_name}")
        print(f"{department_name} employees: {employee_list}")
    return  add_employee

add_to_sales_fn = add_employee_to_department("Sales")
print(add_to_sales_fn)
add_to_engineering_fn = add_employee_to_department("Engineering")
print(add_to_engineering_fn)

add_to_sales_fn("Abc")
add_to_sales_fn("xyz")

add_to_engineering_fn("Chetan")
add_to_engineering_fn("Tejaswee")


def formal_greeting():

    greeting ="How are you doing?"

    def informal_greeting():
        nonlocal greeting #update the local value
        greeting = "Hi there !"
        print("Greeting in the inner function:", greeting)

    informal_greeting()
    print("Greeting in the outer function:",greeting)

formal_greeting()