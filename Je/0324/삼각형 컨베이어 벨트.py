n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))


# Please write your code here.

a_list = l + r +  d
time = t % (3*n)

for _ in range(time):       #time초 반복
    temp = a_list[(3*n) - 1]

    for i in range((3*n) - 1, 0, -1):   #밂
        a_list[i] = a_list[i - 1]

    a_list[0] = temp

for i in range(n):
    print(a_list[i], end=' ')
print()

for i in range(n, (2*n)):
    print(a_list[i], end=' ')
print()

r = a_list[2*n:]
r = r[::-1]
for i in reversed(r):
    print(i, end=' ')
print()
