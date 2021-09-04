# file IO basics
"""
"r" - Open file for reading (Default)
"w" - Open a file for writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode (Default)
"b" - binary mode
"+" - read and write mode
"""

fileText = open("chetan.txt","rt") #file name, modes
content = fileText.read(3) #Read lines of 3 char
print(content)

content = fileText.read(3)
print(content)

print(fileText.readline())

for line in fileText:
    print(line, end=" ")

print(fileText.readlines())
fileText.close()