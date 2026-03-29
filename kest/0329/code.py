A, B = map(int, input().split())

def jjj(n):
    s = str(n)
    return '3' in s or '6' in s or '9' in s

def jjk(n):
    return n % 3 == 0 or jjj(n)

cnt = 0
for i in range(A, B + 1):
    if jjk(i):
        cnt += 1

print(cnt)