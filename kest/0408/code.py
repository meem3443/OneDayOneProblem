n = input()
m = input()

def pan():
    for i in range(len(n) - len(m) + 1):
        same = True
        for j in range(len(m)):
            if n[i + j] != m[j]:
                same = False
                break
        if same:
            return i
    return -1

idx = pan()
print(idx)