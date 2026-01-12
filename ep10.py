# dictonary 
d1 ={}
print(type(d1))

d2 = {"Messi":"Barcelona","Ronaldo":"Juventus", 
      "Suarez":"Inter Miami", 
      "Neymar":{"F":"Santos","S":"Barcelona","T":"Psg"}}
# print(d2["Neymar"])
# d2 ["Mbappe"]= "Real Madrid"
# d2 [520]="Hello"
# print(d2)
# del d2[520]
# print(d2)

# d3 = d2
# del d3["Suarez"]
# print(d2)  This way if you delete element from d3 it will also get deleted from d2

d3 = d2.copy()
del d3["Suarez"]
print(d3)  # this way if you delete element from d3 it will only get deleted from d3 not d2

d2.update({"Sunil":"India"})
print(d2)
print(d2.get("Messi"))
print(d2.keys())
print(d2.items())
print(d2.values())
"""
Dictionary Methods
Dictionary methods are called directly on a dictionary object using dot notation (e.g., my_dict.get()). 
clear(): Removes all items from the dictionary.
copy(): Returns a shallow copy of the dictionary.
fromkeys(keys, value): A class method that creates a new dictionary with specified keys and a default value.
get(key, default): Returns the value for a specified key. If the key is not found, it returns None or a specified default value, avoiding a KeyError.
items(): Returns a view object (a list of tuples) containing each key-value pair as a tuple.
keys(): Returns a view object of all the keys in the dictionary.
pop(key, default): Removes the item with the specified key and returns its value. If the key is not found and a default is provided, it returns the default.
popitem(): Removes and returns the last inserted key-value pair as a tuple (in Python 3.7+). Raises a KeyError if the dictionary is empty.
setdefault(key, default): Returns the value of the key. If the key doesn't exist, it inserts the key with the specified default value and returns the default.
update(other): Adds key-value pairs from other (another dictionary or an iterable of key-value pairs) into the current dictionary. Existing keys are updated with new values.
values(): Returns a view object of all the values in the dictionary. 
Built-in Functions and Operations 
Standard Python functions and operators also interact with dictionaries: 
len(d): Returns the number of key-value pairs in the dictionary d.
del d[key]: Deletes the key-value pair with the specified key from the dictionary. The del keyword can also delete the entire dictionary object.
key in d: Checks if a specified key is present in the dictionary and returns a boolean (True or False).
dict() constructor: Creates an empty dictionary or converts other data structures (like a list of tuples) into a dictionary.
sorted(d): Returns a new list of the dictionary's keys in sorted order.
min(d)/max(d): Returns the minimum/maximum key in the dictionary. 
"""