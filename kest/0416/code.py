n = int(input())

def fi(n):
    if n == 1 :
        return 1
    if n == 2 :
        return 1

    return (fi(n-1) + fi(n-2))

print(fi(n))