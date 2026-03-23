n = int(input())
arr = list(map(int, input().split()))

def insertion_sort(arr):
    size = len(arr)
    for i in range(1,size):
        j = i-1
        key = arr[i]
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

a = insertion_sort(arr)

for i in range(n):
    print(arr[i], end=" ")