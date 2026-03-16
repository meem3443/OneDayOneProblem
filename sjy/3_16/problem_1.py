N = int(input())

arr = []

for _ in range(N):
    line = input().split()
    cmd = line[0]

    if cmd == "push_back":
        arr.append(int(line[1]))
    elif cmd == "pop_back":
        arr.pop()
    elif cmd == "size":
        print(len(arr))
    elif cmd == "get":
        print(arr[int(line[1]) - 1])



