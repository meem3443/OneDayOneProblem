n, m = map(int, input().split())

# Please write your code here.

def nanu(n, m):
    while m:
        n, m = m, n % m
    return n

print(nanu(n, m))
        
