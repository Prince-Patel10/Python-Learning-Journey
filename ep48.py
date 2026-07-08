numbers = ["3","45","18"]

# for items in numbers:
#     items = int(items)
# numbers = list(map(int,numbers))
# print(numbers[1])

# num = [1,2,3,4]
# sq = list(map(lambda x : x*x , num))

# print (sq)

def square(x):
    return x*x

def cube(x):
    return x*x*x

func = [square,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print (val)

l1 = [1,2,3,4,5,6,7,8,9]
def great_5(y):
    return y>5;

pr = list(filter(great_5,l1))
print(pr)

l2 = [1,2,3,4]

sum = reduce(lambda a,b:a+b, l2)
print(sum)