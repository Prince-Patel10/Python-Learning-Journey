#args and kwargs
def funargs(string ,*argsharry,**kwargs):
    print(normal)
    for item in argsharry:
      print(item)
    print("\nRoles of the players")
    for key, value in kwargs.items():
      print(f"{key} 's role is {value}")
har = ["Messi","Ronaldo","Neymar","Lewandoski","Suarez"]
normal = "This are players"
kw = {"Messi ":"GOAT","Ronaldo":"Goalscorer","Neymar":"Playmaker","Suarez":"All in one"}
funargs(normal,*har,**kw)