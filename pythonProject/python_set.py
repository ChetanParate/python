#datastructure set in python

s = set()
print(type(s))
l = [1,2,3,4]
s_from_listOne = set(l)
print(s_from_listOne)
s_from_list = set([1,2,3,4,5])
print(s_from_list)
print(type(s_from_list))

s.add(1)
s.add(2)
print(s)
s.add(2)
print(s)
s1 = s.union({4,5,3})
print(s,s1)
s1.remove(3)
print(s1)
print(s.isdisjoint(s1))