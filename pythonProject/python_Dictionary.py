#key value paires (dictionary) like map in Java
d1 ={"chetan":"burger","teju":"fish","skillf":"roti"}
print(d1)
d2 ={"chetan":{"morning":"burger", "afternoon":"Pizz", "evening":"misalpaw"},"teju":"fish","skillf":"roti"}
print(d2)
d2["vivek"] ="roti"
d2[420] ="kabab"
print(d2)
del d2[420]
print(d2)
d3 = d2.copy()
del d3["skillf"]
print(d3)