class Employee:
    __organization = "ChetSoftTech"

    def __init__(self, name,  department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Salary: {self.__salary}")
        print(f"Organization: {Employee.__organization}")

def create_employee(name, department, salary):
    employee = Employee(name, department, salary)
    return  employee

if __name__ == "__main__":
    print("**************", __name__)
    emp_chet = Employee("Chetan", "Developer", 217000)
    emp_chet.display_details()

def printchet(string):
    return f"Ye string chetan ko de de thakur{string}"

def add(numone, numtwo):
    return numone+numtwo+6

print("and the name is",__name__)
if __name__ == '__main__':
    print(printchet(" Chetan"))
    out = add(4,6)
    print(out)