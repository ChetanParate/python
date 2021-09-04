#String List
grocery = ["harpic","vimbar", "deodrent"]

print(grocery[2])
print(grocery)

#Number List
numbers=[1,34,2,5,67,9]
print(numbers[2])
print(numbers)
numbers.sort()
print(numbers)
print(numbers[1:3])
print(numbers[::1])
print(numbers[::2])
print(numbers[::-2])
numbers.append(34)
print(numbers)
numbers.insert(2,80)
print(numbers)
numbers.pop()
numbers[1]=7
print(numbers)

#tapples - Immutable
taple=(1,2,3)
print(taple)
a = 20
b= 10
print(a,b)
a,b =b,a
print(a,b)