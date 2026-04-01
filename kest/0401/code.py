a, b = map(int,input().split())

def onjeon(i):
    if i % 2 == 0:
        return False
    elif i % 10 == 5:
        return False
    elif (i % 3 == 0) and (i % 9 != 0):
        return False
    else :
        return True

cnt = 0
for i in range(a,b+1):
    if onjeon(i) == True:
        cnt += 1

print(cnt)




