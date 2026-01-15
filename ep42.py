import time

# initial = time.time()
# print(f"Initial time = {initial}")
# print("FOR")
# for i in range(5):
#     time.sleep(1)
#     print("Hello")
# print(f"For loop took {time.time()-initial} seconds")
# j = 0 

# initial2 = time.time()
# print("\nWHILE")
# while(j<=5):
#     print("Hello")
#     j+=1
# print(f"While loop took {time.time()-initial2} seconds")

local_time = time.asctime(time.localtime(time.time()))
local_time2 = time.ctime(time.time())
print(local_time)
print(local_time2)