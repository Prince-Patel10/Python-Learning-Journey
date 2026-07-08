dict = {"BAT":1000, "BOWL":500,"STUMP":700,"SHOES":"2000"}

n = int(input("Enter number of things you want to buy"))
i=1
p1 = 0
while(i<=n):
    a = input("Enter what you want to buy").upper()
    for keys,values in dict.items():
        if(keys==a):
            print(f"Item = {a} and Price = {values}")
            p1+=int(values)
    i+=1
p1 = 0.08*p1 + p1
print("Total bill = ",p1)