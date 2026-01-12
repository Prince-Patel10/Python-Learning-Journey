# a = 6
# b = 9
# c = sum((a,b))
# print(c)

def function1(a,b):
    print("Hello you are a function",a+b)

function1(5,7)

def function2(a,b):
    """
    This is a function which calculates average
    
    :param a: Input
    :param b: Input
    """
    average = (a+b)/2
    # print(average)
    return average

v=function2(6,12)
print(v)
print(function2.__doc__)