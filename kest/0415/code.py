n = int(input())
cnt = 0

def hab(n):
    global cnt

    if n == 1:
        return

    cnt += 1

    if n % 2 == 0:
        hab(n // 2)
    else:
        hab(n // 3)

hab(n)
print(cnt)