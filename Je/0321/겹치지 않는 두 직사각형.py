n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def kadane(arr):
    # 카데인
    cur = arr[0]
    ans = arr[0]

    for x in arr[1:]:
        cur = max(x, cur + x)
        ans = max(ans, cur)

    return ans


def calc(grid, n, m):
    # 최대 직사각형의 합 갱신
    best = [-float('inf')] * (n + 1)

    for r1 in range(n):
        col_sum = [0] * m
        for r2 in range(r1, n):
            for j in range(m):
                col_sum[j] += grid[r2][j]  # 칼럼 합치기

            best[r2 + 1] = max(best[r2 + 1], kadane(col_sum))  # 카데인 돌림

    for i in range(1, n + 1):
        best[i] = max(best[i], best[i - 1])

    return best


top    = calc(grid, n, m)
bottom = calc(grid[::-1], n, m)     # 격자 뒤집어서 활용

grid_t = list(zip(*grid))
left  = calc(grid_t, m, n)
right = calc(grid_t[::-1], m, n)    # 격자 뒤집어서 활용


ans = -float('inf')

for k in range(1, n):   # 수평분할
    ans = max(ans, top[k] + bottom[n - k])

for k in range(1, m):   # 수직분할
    ans = max(ans, left[k] + right[m - k])

print(ans)
