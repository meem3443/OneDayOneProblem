n = int(input())
arr = list(map(int, input().split()))

def selection_sort(arr) :
    for i in range(n-1):
        minimum = i
        for k in range(i + 1, n):
            if arr[k] < arr[minimum]:
                minimum = k

        tmp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = tmp

    for i in range(n):
        print(arr[i], end=" ")

selection_sort(arr)

