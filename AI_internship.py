skills = ["PYTHON","SQL","RAG","DSA","AI"]

print("Enter the skills you have")
choice = str(input().upper())

# for items in skills:
#     if(choice==items):
#         print("You are eligible for AI internship")
#         break
# else:
#      print("Sorry you are not eligible")

if choice in skills:
    print("You are eligible for AI internship")
else:
    print("Sorry you are not eligible")
