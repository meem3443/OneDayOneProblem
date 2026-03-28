A = input()


def Run_Length_Encoding(s):
    string = ""
    count = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count+=1
        else:
            string += s[i-1] +str(count)
            count = 1
    string += s[-1] +str(count)
    return len(string)


if A[0] != A[-1]:
    print(Run_Length_Encoding(A))
else:
    shift =A
    for i in range(len(A) - 1, 0, -1):
        if A[i] != A[i-1]:
            shift = A[i:] + A[:i]
            break
    print(Run_Length_Encoding(shift))
