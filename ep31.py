with open("ep31.txt","r+") as f: #closes the file automatically
    a = f.read(4)
    print(a)
    f.write("Hello")
    