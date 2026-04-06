n = int(input())
arr = list(map(int, input().split()))

def jul(i):
    if i < 0 :
        i = i * -1
    return i

for i in range(n) :
    arr[i] = jul(arr[i])

print (*arr)