#for 반복문을 이용한 코드
N = int(input())

for i in range(N, 101):
    if i >= 90:
        print("A", end=" ")
    elif i >= 80:
        print("B", end=" ")
    elif i >= 70:
        print("C", end=" ")
    elif i >= 60:
        print("D", end=" ")
    elif i < 60:
        print("F", end=" ")

#while 반복문을 이용한 코드
N = int(input())

while N <= 100:
    N = N + 1
    if N >= 91:
        print("A", end = " ")
    elif N >= 81:
        print("B", end =  ' ')
    elif N >=71:
        print("C", end = " ")
    elif N >= 61:
        print("D", end = " ")
    else:
        print("F",end = " ")
    