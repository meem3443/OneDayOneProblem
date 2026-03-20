n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
# 1234순


def count(row, col, L1, L2):
    c_x, c_y = row, col
    move = [L1,L2,L1,L2]
    c_sum =0

    for dx, dy, m in zip(dxs, dys, move):
        for _ in range(m):
            c_x, c_y = c_x + dx, c_y +dy

            if not (0 <= c_x < n and 0 <= c_y < n):
                return 0
            c_sum += grid[c_x][c_y]
    return c_sum

    
max_sum=0 
        
for row in range(1,n):
    for col in range(1,n):

        # 한칸씩
        for L1 in range(1,n):
            for L2 in range(1,n):
                c_sum = count(row, col, L1, L2)

                max_sum = max(c_sum, max_sum)


print(max_sum)
