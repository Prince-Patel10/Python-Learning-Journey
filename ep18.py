# i = 0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue #skip the current iteration
#     print(i+1, end=" ")
#     if i==10:
#         break #stop the loop
#     i=i+1


while(True):
    n1=int(input("Enter input"))
    if n1<100:
        print("Try again")
        continue
    elif n1>=100:
        print("Congratulations")
        break