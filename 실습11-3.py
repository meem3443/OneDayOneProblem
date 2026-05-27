import numpy as np

k = np.arange(0, 9).reshape(3, 3)

sum = k.sum()
c_sum = k.sum(axis=0)
r_sum = k.sum(axis=1)

print(k)
print(sum)
print(c_sum)
print(r_sum)