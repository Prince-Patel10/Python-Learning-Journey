# FILE READING

f = open("ep26.txt","rt")
# print(f.readlines())
# print(f.readline())
# # print(f.readline())
# # print(f.readline())
# content = f.read()
# content = f.read(344)
# print("1",content)

# content = f.read(3)
# print("2",content)

for line in f:
    print(line,end="")
f.close()