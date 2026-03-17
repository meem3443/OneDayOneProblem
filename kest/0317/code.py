N = int(input())

arr = []

for _ in range(N):
    line = input().split()

    if line[0] == "push_back":
        arr.append(int(line[1]))

    elif line[0] == "pop_back":
        arr.pop()

    elif line[0] == "size":
        print(len(arr))

    elif line[0] == "get":
        k = int(line[1])
        print(arr[k - 1])