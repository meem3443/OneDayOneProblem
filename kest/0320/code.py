n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(arr1):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr1[j] > arr1[j + 1]:
                tmp = arr1[j]
                arr1[j] = arr1[j + 1]
                arr1[j + 1] = tmp

    for k in range(n):
        print(arr1[k], end=" ")

bubble_sort(arr)