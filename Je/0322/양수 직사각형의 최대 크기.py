n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def max_rect(hist):
    stack = []
    max_sum = 0

    for i, h in enumerate(hist):
        while stack and hist[stack[-1]] > h:
            height = hist[stack.pop()]
            left = stack[-1] if stack else -1
            max_sum = max(max_sum, height * (i - left - 1))
        stack.append(i)

    while stack:
        height = hist[stack.pop()]
        left = stack[-1] if stack else -1
        max_sum = max(max_sum, height * (len(hist) - left - 1))

    return max_sum



hist = [0] * m
max_sum = 0


for i in range(n):
    for j in range(m):
        hist[j] = hist[j] + 1 if grid[i][j] > 0 else 0  # 히스토그램 갱신

    max_sum = max(max_sum, max_rect(hist))


if max_sum == 0: max_sum = -1
print(max_sum)
