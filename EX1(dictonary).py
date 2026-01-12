d = {"Mutable":"Can be changed","Immutable":"Cannot be changed","Barcelona":"https://en.wikipedia.org/wiki/FC_Barcelona","Rohit":"https://en.wikipedia.org/wiki/Rohit_Sharma"}
print("Enter the word to get info about it : Mutable,Immutable,Barcelona,Rohit Sharma")
ip = input().capitalize()
print("The meaning is : ", d.get(ip))