n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.


def shift(row, dir):
    if dir == 'L':
        a[row] = [a[row][-1]] + a[row][:-1]
    else:
        a[row] = a[row][1:] + [a[row][0]]

for row, d in winds:
    r = row -1
    shift(r, d)

    #d위
    c_d=d
    for i in range(r, 0, -1):
        is_shift = False
        for j in range(m):
            if a[i][j] == a[i-1][j]:
                is_shift = True
                break   
        if is_shift:
            c_d ='R' if c_d == 'L' else 'L'
            shift(i-1, c_d)
        else:
            break
            

    #아래
    c_d=d
    for i in range(r, n-1):
        is_shift = False
        for j in range(m):
            if a[i][j] == a[i+1][j]:
                is_shift = True
                break   
        if is_shift:
            c_d ='R' if c_d == 'L' else 'L'
            shift(i+1, c_d)
        else:
            break
            
for r in a:
    print(*r)
