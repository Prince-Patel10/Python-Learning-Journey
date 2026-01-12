f=open("ep30.txt")
# print(f.tell())
print(f.readline())
# print(f.tell()) # gives the location of pointer
f.seek(0) #brings pointer to given location
print(f.readline())
# print(f.tell())
f.close()