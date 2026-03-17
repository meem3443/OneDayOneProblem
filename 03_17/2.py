n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

total = 0

for i in range(n):
    count =1
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
            count +=1
        else:
            count = 1
        if count >= m:
            total +=1
            break
    
for i in range(n):
    count =1
    for j in range(n-1):
        if grid[j][i] == grid[j+1][i]:
            count+=1
        else:
            count = 1
        if count >= m:
            total+=1
            break

if(m==1):
    print(n*2)
else:
    print(total)
