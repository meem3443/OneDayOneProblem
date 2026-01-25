def recursionPrint(N: int):
    if N <= 0:
        return
    print(N, end=" ")
    recursionPrint(N-1) 
    print(N, end=" ")


N = int(input())
recursionPrint(N)
    