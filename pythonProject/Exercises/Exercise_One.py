# Create a DICTIONARY haveing some values & take input from user to check the meaing of that work which is present in dictionary

myDictionary = {
    "One": "Ek",
    "Two": "Don",
    "Three": "Tin",
    "Fore": "Char",
    "Five": "Pach"
}

print("Enter the any word between One to Five to Know meaing in Marath :")
num = input()
print(myDictionary[num.capitalize()])