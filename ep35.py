# lambda functions
# def minus(a,b):
#     return a-b
minus = lambda a,b : a-b

print(minus(9,4))

# def a_first(a):
#     return a[1]

a = [[1,14],[5,6],[8,23]]
# a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)