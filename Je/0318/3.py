n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shapes = [
    [(0,0), (0,1), (0,2)], [(0,0), (1,0), (2,0)], 
    [(0,0), (1,0), (1,1)], [(0,1), (1,0), (1,1)], [(0,0), (0,1), (1,1)], [(0,0), (0,1), (1,0)]
]

def count_sum(y, x):
    l_max =0
    for s in shapes:
        c_sum = 0

        for dy, dx in s:
            n_dy, n_dx = y + dy, x + dx
            if (0<= n_dy < n and 0 <= n_dx < m):
                c_sum += grid[n_dy][n_dx]
            else:
                c_sum =0
                break
        if l_max < c_sum: l_max = c_sum

    return l_max


max_sum =0

for i in range(n):
    for j in range(m):
        tem = count_sum(i,j)
        if max_sum < tem:
            max_sum = tem

print(max_sum)



