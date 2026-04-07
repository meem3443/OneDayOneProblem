A = list(input())

def pan():
    for i in range(len(A)):
        if A[i] != A[0]:
            return True
    return False

if pan():
    print("Yes")
else:
    print("No")