# var1=6
# var2=56

# var3=int(input())

# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [1,2,3,4]
# print(4 in list1)
# if 4  in list1:
#     print("Yes")
# print(5 not in list1)

age = int(input("Enter your age"))
if age>18:
    if(age >100):
        print("Illogical AGE")
    else:
        print("You are eligible to drive")
elif age==18:
    print("Come physically for test")
else:
    if(age<=5):
        print("Illogical AGE")
    else:
        print("You are not eligible to drive")