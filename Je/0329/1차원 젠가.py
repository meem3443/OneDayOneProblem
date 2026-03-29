n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
temp = blocks[:s1-1] + blocks[e1:]
a = temp[:s2-1] + temp[e2:]


print(len(a))
for i in a:
    print(i)
