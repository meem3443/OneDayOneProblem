N = int(input())

cnt = 0
cnt1 = 0

for num in range(N):
    num = int(input())
    if num % 3 == 0:
        cnt += 1
    if num % 5 == 0:
        cnt1 += 1
        
print(cnt, cnt1, end = " ")


# 7
# 42
# 10
# 54
# 34
# 55
# 57
# 60
# 30
# 50