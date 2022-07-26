from python_import_one import create_employee
import python_import_one

if __name__ == "__main__":
    print("**************", __name__)
    emp_chet = python_import_one.Employee("Chetan", "Developer", 217000)
    emp_chet.display_details()
    print("*********************************")
    emp_teju = create_employee("Tejaswee","DotNet Developer", 110000)
    emp_teju.display_details()

print(python_import_one.add(5,8))