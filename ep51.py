def f1():
    print("hi")

f2 = f1()
print(f2)

def d1(a):
    def d2():
        print("Executing")
        a()
        print("Done")
    return d2
@d1
def e():
    print("Prince")

e()
