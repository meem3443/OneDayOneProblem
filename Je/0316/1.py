n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def count_coin(x, y):
    count =0
    for i in range(y, y+3):
        for j in range(x, x+3):
            count += grid[i][j]

    return count

c =0
for i in range(n-2):
    for j in range(n-2):
        a =count_coin(i,j)
        if c < a:
            c = a
        
print(c)
