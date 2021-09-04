
#Health Managment System
def getdate():
    import datetime
    return  datetime.datetime.now()

client_list = {1:"chetan", 2:"Tejaswee", 3:"Someone"}
log_list = {1:"Exercise", 2:"Diet"}

try:
    print("Select the Client Name: ")
    for key,value in client_list.items():
        print("Press ",key,"for ",value,"\n",end="")
    client_name = int(input("Enter your choice :\n"))

    print("*********************************************")
    print("Selected Client : ", client_list[client_name], "\n", end="")
    print("*********************************************")
    print()
    print("Press 1 for Logs")
    print("Press 2 for Retrieve")
    opt = int(input())

    if opt == 1:
        for key,value in log_list.items():
            print("Press", key, "to log", value,"\n", end="")
        log_name = int(input())
        print("*********************************************")
        print("Seleted job : ",log_list[log_name])
        print("*********************************************")
        filew = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        keys ="Y"
        while(keys.lower() != "N".lower()):
            print("Enter",log_list[log_name],"\n", end="")
            my_txt =input()
            filew.write("["+str(getdate())+"]:"+my_txt+"\n")
            keys = input("Add more ? Y/N:")
            continue
        filew.close()
    elif opt == 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_name = int(input("Enter "))
        print(client_list[client_name],"-",log_list[log_name],"Report :","\n",end="")
        filer = open(client_list[client_name] + "_" + log_list[log_name] + ".txt")
        contents = filer.readlines()
        for line in contents:
            print(line,end="")
        filer.close()
    else:
        print("Invalid Input !!!")
except Exception as ex:
    print("Wrong Input !!!")




##############
def takeoperation(opt):
    if opt == 1:
        can =int(input("Enter 1 for Excercis & 2 for food :"))
        if(can == 1):
            value = input("Type here\n")
            with open("chetan-ex.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
                print("Successfully file Written....")
        elif(can == 2):
            value = input("Type here\n")
            with open("chetan-food.txt","a") as op:
                op.write(str([str(getdate())])+": "+value+"\n")
            print("Successfully file Written....")
    elif opt == 2:
        can = int(input("Enter 1 for Excercis & 2 for food :"))
        if (can == 1):
            value = input("Type here\n")
            with open("tejaswee-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully file Written....")
        elif (can == 2):
            value = input("Type here\n")
            with open("tejaswee-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully file Written....")
    elif opt == 3:
        can = int(input("Enter 1 for Excercis & 2 for food :"))
        if (can == 1):
            value = input("Type here\n")
            with open("someone-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully file Written....")
        elif (can == 2):
            value = input("Type here\n")
            with open("someone-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully file Written....")
    else:
        print("Please enter the valid imput(1-chetan, 2-tejaswee, 3-someone)")

def retrieve(opt):
    if opt == 1:
        can = int(input("Enter 1 for Excercis & 2 for food :"))
        if (can == 1):
            with open("chetan-ex.txt") as op:
               for i in op:
                   print(i,end="")
        elif (can == 2):
            with open("chetan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif opt == 2:
        can = int(input("Enter 1 for Excercis & 2 for food :"))
        if (can == 1):
            with open("tejaswee-ex.txt") as op:
               for i in op:
                   print(i,end="")
        elif (can == 2):
            with open("tejaswee-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif opt == 3:
        can = int(input("Enter 1 for Excercis & 2 for food :"))
        if (can == 1):
            with open("someone-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (can == 2):
            with open("someone-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter the valid input(1-chetan, 2-tejaswee, 3-someone)")

# print("Health Managment System : ")
# invalue = int(input("Press 1 for write the value OR 2 for retrieve :"))
#
# if invalue == 1`  :
#     opt = int(input("Press 1 for Chetan, 2 for Teju and 3 for someone :"))
#     takeoperation(opt)
#
# else:
#     opt = int(input("Press 1 for Chetan, 2 for Teju and 3 for someone :"))
#     retrieve(opt)