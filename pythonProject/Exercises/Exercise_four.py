#find the numeric value from the list and print the greater than 6 value
items =[int,float,"Chetan", 4,6,4,3,67,78,5,3,56,90]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)