mylist = ["abc", "def","ghi","jkl","mno","pqr","stu"]

for item in mylist:
    print(item," and ",end=" ")

joinedlist = ", ".join(mylist)
print(joinedlist, "other alphabases")