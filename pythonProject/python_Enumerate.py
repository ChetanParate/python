list =["Bhindi","Aloo", "chopsticks", "Chowmeins"]

i = 1
for item in list:
    if i%2 == 0:
        print(f"Chetya please buy {item}")
    i += 1

for index,item in enumerate(list):
    if index%2==0:
        print(f"Chetya please buy {item}")