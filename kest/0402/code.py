n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def yeon(n1, n2):
    for i in range(n1 - n2 + 1):
        if a[i] == b[0]:
            check = True
            for k in range(1, n2):
                if a[i + k] != b[k]:
                    check = False
                    break
            if check:
                return True
    return False

if yeon(n1, n2) == True:
    print("Yes")
else:
    print("No")