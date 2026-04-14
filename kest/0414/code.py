n = int(input())

def hab(n):
    if n < 10 :
        return n*n

    return hab(n//10)+(n%10)*(n%10)

print(hab(n))