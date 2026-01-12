# 45*3 = 555, 56+9= 77, 56/6 = 4
print("Enter 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
choice = int(input())
n1 = int(input("Enter number 1"))
n2 = int(input("Enter number 2"))

if choice==1:
    if n1==56 and n2==9:
        print(77)
    else:
        print("Addition is : ",n1+n2)
elif choice==2:
    print("Subtraction is : ",n1-n2)
elif choice==3:
    if n1==45 and n2==3:
        print(555)
    else:
        print("Multiplication is : ",n1*n2)
elif choice==4:
    if n1==56 and n2==6:
        print(4)
    else:
        print("Division is : ",n1/n2)
else:
    print("Invalid inputs")