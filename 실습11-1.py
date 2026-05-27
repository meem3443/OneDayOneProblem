import numpy as np

noise = np.random.rand(10, 10)

a=noise.max()
b=noise.min()

print("최솟갑 =", a)
print("최댓값 =", b)