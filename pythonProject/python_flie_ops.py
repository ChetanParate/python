file = open("chetan.txt")
print(file.tell()) #pointer is present
print((file.readline()))
file.seek(10)
print((file.readline()))
file.close()
