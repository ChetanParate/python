numbers =[100,300,200,400,700,800]

number_copy = []
for number in numbers:
    number_copy.append(number)

print(number_copy)

number_copy_using_comprehension = [number for number in numbers]
print(number_copy_using_comprehension)

number_copy_using_comprehension = [number * number for number in numbers]
print(number_copy_using_comprehension)

print ([x * x for x in range(20) if x % 2 ==0])

shapes =["Square","Circle","Triangle"]
colors =["Red","Blue","Green"]
#nested for loop
combined = [(color, shape) for shape in shapes for color in colors]
print(combined)


num  = [(i,"Even") if i % 2 == 0 else (i, "Odd") for i in range(8)]
print(num)

output_generator =(x * x for x in numbers)# generator statment
print(output_generator)

list_from_generator = list(output_generator)
print(list_from_generator) # generator statefull
