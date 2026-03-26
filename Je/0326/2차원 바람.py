n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    temp = grid[r1][c1]
    
    for r in range(r1, r2):
        grid[r][c1] = grid[r+1][c1]
    for c in range(c1, c2):
        grid[r2][c] = grid[r2][c+1]

    for r in range(r2, r1, -1):
        grid[r][c2] = grid[r-1][c2]
    for c in range(c2, c1 + 1, -1):
        grid[r1][c] = grid[r1][c-1]
    
    grid[r1][c1+1] = temp


    n_grid = [row[:] for row in grid]

    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            total = grid[r][c]
            cnt = 1
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
              
                if 0 <= nr < n and 0 <= nc < m:
                    total += grid[nr][nc]
                    cnt += 1
            
            n_grid[r][c] = total // cnt
            
    grid = n_grid
    

for row in grid:
    print(*(row))
