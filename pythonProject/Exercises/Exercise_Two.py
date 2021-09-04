#Quize
print("******* Driving Eligiblity Check *******")
print("What is your Age?")
age = int(input("Please enter you Age :"))

if age>18:
    print("Yes, You are eligible to drive a car")
elif age == 18:
    print("Need to you check policy, Please come with identification")
else:
    print("You are not eligible to drive a car")