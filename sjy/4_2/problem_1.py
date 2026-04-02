n, m = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):  
        if num % i == 0:
            return False
    return True

total = 0
for i in range(n, m + 1):
    if is_prime(i):
        total += i

print(total)
