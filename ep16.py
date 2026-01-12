#for loops
# l1= ["Messi","Ronaldo","Neymar","Suarez"]
# for items in l1:
# print(items)
# l2= [["Messi",1300],["Ronaldo",1000],["Neymar",900],["Suarez",800]]
# for item,contribution in l2:
#     print(item , "has", contribution, "goal/assist contributions")
#     #print(items)
# dict1 = dict(l2)
# print(dict1)

# for items,contribution in dict1.items():
#     print(items , "has", contribution, "goal/assist contributions")
# for item in dict1:
#     print(item)

l3 = ["Harry",5,3,3,22,21,64,23,233,23]

for item in l3:
    if str(item).isnumeric() and item>6:
        print(item)