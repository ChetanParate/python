import time

initial = time.time()
print(initial)

k = 0
while(k<45):
    print("This is bad boy chetan")
    time.sleep(1)
    k += 1
print(f"While loop ran in : {time.time()-initial} Seconds")

initialOne = time.time()

for i in range (45):
    print("This is good to see you chetan")
print(f"For loop ran in : {time.time()-initialOne} Seconds")

#Formated time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)