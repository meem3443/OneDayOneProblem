n = int(input())

def hab(n):
    if n == 1:
        return 1

    return hab(n-1)+n

print(hab(n))