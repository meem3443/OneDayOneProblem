N = int(input())
num = list(map(int, input().split()))
num1 = []

for i in range(N):
     if num[i] % 2 == 0:
          num1.append(num[i])
num1.reverse()

for j in num1:
     print(j, end = " ")