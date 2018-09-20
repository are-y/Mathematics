size = 18

count = 1000

arr = ['*'] * count

arr1 = []

for i in range(2, count):
    for j in range(2, i):
        if i % j == 0:
            # print(i)
            break
    else:
        # print(i,end=' ')
        arr[i - 1] = str(i)
        arr1.append(i)

array = [arr[i:i + size] for i in range(0, len(arr), size)]

for x in array:
    for f in x:
        print("".join(f).rjust(10), end='')
    print("\n")

arr2 = []

for i, v in enumerate(arr1):
    if i > 0:
        # print(v-arr1[i-1])
        arr2.append(v - arr1[i - 1] - 1)

from collections import Counter

result = Counter(arr2)

print(result)

import numpy as np
import matplotlib.pylab as plt

# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # 定义域为： -2pi 到 2pi
plt.figure(50, dpi=80)  # 创建图表1

for item in result.keys():
    print(item,result[item])
    plt.plot(item,result[item])
# for i in range(1, 5):  # 画四条线
#     plt.plot(x, np.sin(x / i))

plt.show()



