_list = [[2, 0, 1, 5],
         [0, 4, 1, 1],
         [1, 4, 0, 0]]

def f(b):
    for i in range(4):
        _list[b][i] = _list[(b + 1) % 3][(i + 1) % 4]

f(1)
f(2)
f(0)
result = 0

for i in range(3):
    result += _list[i][(i + 1) % 4]
print(result)
