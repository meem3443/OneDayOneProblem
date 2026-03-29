n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())


# Please write your code here.

# 터진부분 0 후 temp 에 적립 >교채

dxs, dys = [0,1,0,-1], [1,0,-1,0]
x, y = x-1, y-1
l = grid[x][y]
for i in range(l):
    for dx, dy in zip(dxs,dys):           #사방
        n_x, n_y = x+i*dx, y+i*dy
        if( 0 <= n_x < n and 0 <= n_y <n ):
            grid[n_x][n_y] = 0

new_grid = [[0] * n for _ in range(n)]

for col in range(n):
    temp = []
    for row in range(n-1, -1, -1):
        if grid[row][col] !=0:
            temp.append(grid[row][col])
    
    for i in range(len(temp)):
        new_grid[n - 1 - i][col] = temp[i]

for row in new_grid:
    print(*row)
