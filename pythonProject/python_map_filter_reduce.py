numbers =["7","17","27","37","77"]

#***********************************************map function
numbers = list(map(int, numbers))

#map string numbers to int numbers
#first way

# for items in range(len(numbers)):
#     numbers[items] = int(numbers[items])


numbers[2] = numbers[2]+1
print(numbers[2])

num = [2,3,4,5,7,8,78,455,90]
square = list(map(lambda x:x*x,num))
print(square)


def squ(a):
    return a*a
def cube(a):
    return a*a*a
func =[squ,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

#********************************************Filters
num_one = [2,3,4,5,7,8,78,455,90]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5, num_one))
print(gr_than_5)


#**********************************************Reduce

from functools import reduce
num_two = [2,3,4,5,7,8]
nums = reduce(lambda x,y:x+y, num_two)
print(nums)
#print(2+3+4+5+7+8)



