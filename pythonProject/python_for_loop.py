#for look using list

list1 = ["one","two","three","four"] #list
list2 = ("one","two","three","four") #tuple
list3 = [["one",1],["two",2],["three",3],["four",4]] #list
for item in list1:
    print(item)
for item in list2:
    print(item)
for item1, item2 in list3:
    print(item1,item2)
dic = dict(list3)
for item1, item2 in dic.items():
    print(item1,item2)

for letter in "Chetan":
    print(letter)

for char in "Chetan is good boy":
    print(char)
for name in "chetan","teju", "roshan", "vivek":
    print(name)