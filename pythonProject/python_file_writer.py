f = open("chetan.txt", "w")
f.write("Chetan you the boss of my life\n")
print(f)

#Handle read and write
f = open("chetan.txt","r+")
print(f.read())
f.write("Chetya is chetya ")
f.close()