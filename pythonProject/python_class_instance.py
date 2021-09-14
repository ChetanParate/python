class Employee:
    no_of_leaves = 9
    pass

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

