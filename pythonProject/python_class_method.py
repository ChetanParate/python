class Employee:
    no_of_leaves = 9

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}, and Role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        param = string.split("-")
        return cls(*string.split("-"))
        # return cls(param[0],param[1],param[2])

    @staticmethod
    def printgood(string):
        print("This is good to know "+string)
        return "You are too good"


motu = Employee("Motya",6767,"creator")

chet = Employee.from_str("Chetya-7777-newway")



motu.change_leaves(20)

print(Employee.no_of_leaves)
print(chet.name)
print(chet.printgood("Chetan"))
