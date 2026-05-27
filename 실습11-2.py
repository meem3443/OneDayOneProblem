import numpy as np

k = np.random.rand(3, 3)

mean = k.mean()
std = k.std()

normalized = (k - mean) / std

print(normalized)