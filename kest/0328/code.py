n = int(input())

def number(n):
    count = 0

    for i in range(n+1) :
        count += i

    return(count // 10)

a = number(n)
print(a)


