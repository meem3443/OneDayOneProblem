n = int(input())

def hab(n):
    if n == 1 :
        return 1
    if n ==2 :
        return 2

    return hab(n-2) + n

print(hab(n))