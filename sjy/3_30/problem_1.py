n = int(input())

# Please write your code here.

def add(a, b):
    cnt = sum(range(a, b + 1))
    return cnt // 10
print(add(1, n))
        
        