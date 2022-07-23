l = 10 #Global variable
x = 89
def fuctionOne (n):
    # l = 5 #Local Variable
    m = 8
    global l
    l =l+45
    print(l)
    print(n,"I have printed local value")

fuctionOne("This is chetan")
print(l)

def harry():
    x = 20
    def chet():
        global  x
        x = 88
    print("Before calling chet () ", x)
    chet()
    print("after calling chet () ", x)
harry()
print(x)