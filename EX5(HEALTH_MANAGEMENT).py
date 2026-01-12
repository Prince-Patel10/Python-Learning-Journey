def getdate():
    import datetime
    return datetime.datetime.now()
def log_retrieve():
    print("Press \n1 for log \n2 for retrieve")
    choice = int(input())

    print("Enter \n1 for Harry \n2 for Rohan" \
    "\n3 for Hammad")
    client = int(input())

    print("Enter \n1 for exercise \n2 for diet")
    log = int(input())

    if(choice==1):
        if(client==1):
            if(log==1):
                with open("Harry(exercise).txt","a+") as f:
                    print("Enter the exercise you did")
                    exercise = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(exercise)
                    f.write("\n")
                    
            elif(log==2):
                with open("Harry(diet).txt","a+") as f:
                    print("Enter the food you had")
                    diet = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(diet)
                    f.write("\n")
        elif(client==2):
            if(log==1):
                with open("Rohan(exercise).txt","a+") as f:
                    print("Enter the exercise you did")
                    exercise = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(exercise)
                    f.write("\n")
            elif(log==2):
                with open("Rohan(diet).txt","a+") as f:
                    print("Enter the food you had")
                    diet = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(diet)
                    f.write("\n")
        elif(client==3):
            if(log==1):
                with open("Hammad(exercise).txt","a+") as f:
                    print("Enter the exercise you did")
                    exercise = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(exercise)
                    f.write("\n")
            elif(log==2):
                with open("Hammad(diet).txt","a+") as f:
                    print("Enter the food you had")
                    diet = str(input())
                    v = getdate()
                    f.write("Time " + str(v) + "\n")
                    f.write(diet)
                    f.write("\n")
    
    elif(choice==2):
        if(client==1):
            if(log==1):
                f = open("Harry(exercise).txt","r+")
                # for line in f:
                #     print(line,end="")
                print(f.read())
                f.close()
            elif(log==2):
                f = open("Harry(diet).txt","r+")
                for line in f:
                    print(line,end="")
                f.close()
        elif(client==2):
            if(log==1):
                f = open("Rohan(exercise).txt","r+")
                for line in f:
                    print(line,end="")
                f.close()
            elif(log==2):
                f = open("Rohan(diet).txt","r+")
                for line in f:
                    print(line,end="")
                f.close()
        elif(client==3):
            if(log==1):
                f = open("Hammad(exercise).txt","r+")
                for line in f:
                    print(line,end="")
                f.close()
            elif(log==2):
                f = open("Hammad(diet).txt","r+")
                for line in f:
                    print(line,end="")
                f.close()

    return 
                
log_retrieve()


# f = open("Harry(exercise).txt","a+")
# print("Enter the exercise you did")
# exercise = str(input())
# v = getdate()
# f.write("Time " + str(v) + "\n")
# f.write(exercise)
# f.write("\n")
# f.close()