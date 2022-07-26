class Employee:
    no_of_leaves = 9

   # def __init__(self,name,salary,role):
    #     self.name = name
     #    self.salary = salary
      #   self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}, and Role is {self.role}"

# motu = Employee("Motya",6767,"creator")
chetan = Employee()
teju = Employee()


chetan.name = "Chetan"
chetan.salary = 455
chetan.role = "Instructor"

teju.name = "Tejaswee"
teju.salary = 1000
teju.role = "student"
print(Employee.no_of_leaves)
teju.no_of_leaves = 10
print(teju.no_of_leaves)
print(chetan.__dict__)
print(teju.__dict__)
print(Employee.__dict__)
print(chetan.printdetails())

