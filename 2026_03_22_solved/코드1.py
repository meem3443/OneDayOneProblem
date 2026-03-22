n1, n2 = list(map(int, input().split()))
arr = []

arr.append(n1)
arr.append(n2)

for i in range(2, 10):
    arr.append((arr[i-2] + arr[i-1]) % 10)

for o in arr:
    print(o, end = " ")
