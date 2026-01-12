# GLOBAL, LOCAL VARIABLE
# l = 10 #global variable
# def f1(n):
#     # l = 5 # local variable
#     m = 20 # local variable
#     global l
#     l = l + 45
#     print(l,m)
#     print(n + " I have printed")

# f1("Yes")

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan ",x)
    rohan()
    print("after calling rohan ",x)

harry()
print(x)