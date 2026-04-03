cnt = 0
cnt1 = 0

for num in range(10):
    num = int(input())
    if num % 3 == 0:
        cnt += 1
    if num % 5 == 0:
        cnt1 += 1
        
print(cnt, cnt1, end = " ")