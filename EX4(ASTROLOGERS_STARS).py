# Pattern printing
""" 
Integer n
Boolean = True or False (input 1 or 0)

for n=4
True 
*
**
***
****

False
****
***
**
*
"""
print("Enter number for astrologers star printing")
num = int(input())

print("Enter 0 or 1")
temp = int(input())

result = bool(temp)
print(result)

if(result==True):  # 1 = true
    for i in range(0,num,1):
        i = i + 1
        print(i * "* ")

if(result==False): # 0 = false
    for i in range(num,0,-1):
        print(i * "* ")
        i = i + 1