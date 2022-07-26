import sys
from python_import_one import create_employee

if __name__ == "__main__":

   #print("Number of command line arguments: ", len(sys.argv))
   #print("Script name: ",sys.argv[0])
    print("All arguments: ", sys.argv)

    name = sys.argv[1]
    department = sys.argv[2]
    salary = int(sys.argv[3])

    emp = create_employee(name, department, salary)
    emp.display_details()