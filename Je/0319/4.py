n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def get_cost(k):
    return k * k + (k + 1) * (k + 1)


def count_g(row, col, k):
    c_gold =0

    for r in range(row - k, row + k + 1):
        for c in range(col - k, col + k + 1):

            if 0 <= r < n and 0 <= c < n:
                if abs(r - row) + abs(c - col) <= k:
                    if grid[r][c] == 1:
                        c_gold += 1
    return c_gold


max_gold = 0

for i in range(n):
    for j in range(n):
        for k in range(2 * n - 1):
            current_gold = count_g(i, j, k)
            cost = get_cost(k)

            if current_gold * m >= cost: 
                if current_gold > max_gold:
                    max_gold = current_gold


print(max_gold)
