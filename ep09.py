grocery = ["Tomato", "Cucumber","Potato","Onion","Carrot",56]
print(grocery)
print(grocery[2])
numbers = [2,7,3,11,9]
print(numbers[4])
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
print(numbers[0:5])
# list reverse
print(numbers[::-1])
# list element skip
print(numbers[0:5:2])
print(min(numbers))
print(max(numbers))
# list functions
numbers.append(8)
print(numbers)

numbers.insert(3,13)
print(numbers)

numbers.pop()
print(numbers)

numbers[1]=76
print(numbers)

# tuple
tp = (1,2,3)
# tp(2)=4 not possible
print(tp)

# list is mutable
# tuple is immutable

# swapping numbers
a = 8
b = 2
# temp = a
# a = b
# b = temp
a,b=b,a
print(a,b)
"""
List Methods
List methods are called using the dot syntax on a list instance (e.g., my_list.append(item)). These methods generally modify the list in place and return None. 
append(element): Adds a single element to the end of the list.
extend(iterable): Appends elements from an iterable (like another list, tuple, or string) to the current list.
insert(index, element): Inserts an element at the specified index, shifting subsequent elements to the right.
remove(element): Removes the first occurrence of the specified element by value.
pop([index]): Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element.
clear(): Removes all elements from the list, making it empty.
index(element, [start, end]): Returns the zero-based index of the first occurrence of the element. A ValueError is raised if the element is not found.
count(element): Returns the number of times the specified element appears in the list.
sort(key=None, reverse=False): Sorts the items of the list in place (ascending by default). Optional parameters customize the sort order.
reverse(): Reverses the order of the elements in the list in place.
copy(): Returns a shallow copy of the list. 
Built-in Functions
These functions are used with lists but are general-purpose functions in Python, called on the list as an argument (e.g., len(my_list)). 
len(list): Returns the total number of elements in the list.
max(list): Returns the largest item in the list.
min(list): Returns the smallest item in the list.
sum(list): Returns the sum of all elements in the list (must be numeric).
list(iterable): Converts an iterable (like a tuple, string, or range) into a list.
sorted(iterable): Returns a new sorted list from the items in an iterable, without modifying the original.
enumerate(iterable): Returns an enumerate object, which produces pairs of an index and the item at that index when iterated over. 
"""