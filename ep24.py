num1 = input("Enter num 1")
num2 = input("Enter num2")
try:
    print("Sum is ",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")