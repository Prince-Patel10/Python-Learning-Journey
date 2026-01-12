# modules
import random
import math
import os
import time

start_time = time.perf_counter()

random_number = random.randint(0,5)
# print(random_number)
rand = random.random()*100
# print(rand)
lst = ["Star plus","DD1","Aaj Tak","CodeWithHarry"]
choice = random.choice(lst)
print(choice)

print(math.pi)
print(math.sqrt(4))
print(math.factorial(5))

print(os.getcwd())
print(os.cpu_count())

print(time.time())
print(time.gmtime())

end_time = time.perf_counter()

execution_time = end_time - start_time

print(f"Time at start {start_time} \n Time at end {end_time} \n Time taken for execution {execution_time}")