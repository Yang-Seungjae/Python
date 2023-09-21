import numpy as np
import time
import random

arr_a = np.random.rand(100000000)
arr_b = np.random.rand(100000000)
result = np.zeros(100000000)
start=time.time()
for i in range(len(arr_a)):
    result[i]=arr_a[i]*arr_b[i]
end=time.time()
print("소요시간: ", end-start)





