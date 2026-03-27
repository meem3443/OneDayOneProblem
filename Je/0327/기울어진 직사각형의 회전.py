n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c, m1, m2, m3, m4, D = map(int, input().split())


dxs_0, dys_0 = [-1, -1, 1, 1], [1, -1, -1, 1]
dxs_1, dys_1 = [-1, -1, 1, 1], [-1, 1, 1, -1]

def shift(row, col, L1, L2, D):
    temp = grid[row][col]
    c_x, c_y = row, col
    
    dxs, dys = dxs_0, dys_0           #시계방향 이동 -> 당기기 순회는 반시계방향
    move = [L1,L2,L1,L2]
    if D == 0:                        #반시계 방향 이동 -> 당기기 순회는 시계방향
        dxs, dys = dxs_1, dys_1 
        move = [L2,L1,L2,L1]

    
    for dx, dy, m in zip(dxs, dys, move):
        for _ in range(m):
            n_x, n_y = c_x + dx, c_y +dy              #다음 좌표
            grid[c_x][c_y] = grid[n_x][n_y]           #한칸씩 당기기
            c_x, c_y = n_x, n_y                       #좌표 갱신

    
    dxs, dys = dxs_0, dys_0                           #진실된 방향......
    if D == 1:                
        dxs, dys = dxs_1, dys_1
    for dx, dy in zip(dxs, dys):
        n_x, n_y = c_x + dx, c_y +dy        
        grid[n_x][n_y]  = temp
        break
    return


r, c = r-1, c-1

shift(r, c, m1, m2, D)
for row in grid:
    print(*row)
