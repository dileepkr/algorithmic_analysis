import random, timeit
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

nums = []
l_times = []
d_times = []

for i in range(10000, 1000001, 100000):
    t = timeit.Timer(f"random.randint(a=0,b={i}) in x", "from __main__ import x, random")
    nums.append(i)

    x = list(range(i))
    lst_time = t.timeit(number=10)
    l_times.append(lst_time)

    x= {j:None for j in range(i)}
    dict_time = t.timeit(number=10)
    d_times.append(dict_time)

fig, ax = plt.subplots()
ax.scatter(nums, l_times)
ax.scatter(nums, d_times)

plt.show()

