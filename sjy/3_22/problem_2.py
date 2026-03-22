n, m = map(int, input().split())

# Please write your code here.

def min(n, m):
    while(m > 0):
        n, m = m, n % m
    return n
result = (m * n) // min(n, m)

print(result)