#recursion
def factorial_recursive(n):
    """
    Docstring for factorial
    gives factorial 
    """
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        i+=1
        fac = fac*i
    return fac
    
number = int(input("Enter number to find factorial"))
print(factorial_recursive(number))
print(factorial_iterative(number))

#fibonacci
def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
       return fibonnaci(n-2) + fibonnaci(n-1)
    
print(fibonnaci(number))
    