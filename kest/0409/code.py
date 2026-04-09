n, m = map(int, input().split())
A = list(map(int, input().split()))

def pan(m):
    cnt = 0

    while True:
        cnt += A[m - 1]

        if m == 1:
            break

        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return cnt

print(pan(m))