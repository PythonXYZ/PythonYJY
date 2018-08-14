import time, numpy as np

num_list = list(np.arange(0, 100000000, 1))
result_list = []

start = time.time()

for item in num_list:
    if item%2 == 0:
        result_list.append(item)
    else:
        result_list.append(item + 1)

end = time.time()

print(end - start)

start = time.time()

def new_function(item):
    if item%2 == 0:
        result_list.append(item)
    else:
        result_list.append(item + 1)
        
x = map(new_function, num_list)

end = time.time()

print(end - start)

