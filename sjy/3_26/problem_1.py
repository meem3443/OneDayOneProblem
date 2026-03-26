n = int(input())
gidung = list(map(int, input().split()))
count = 0



for j in range(n):
    while gidung[j] != min(gidung):
        count += 1
        gidung[j] -= 1
    

print(count)
   



