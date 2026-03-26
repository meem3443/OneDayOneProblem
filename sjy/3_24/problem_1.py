a, b = map(int, input().split())

# Please write your code here.



def tsn(n, m):

    global count
    count = 0
    
    for i in range(n, m):
        if i % 3 == 0:
            count += 1
        s = str(i)
    # 3, 6, 9가 포함되어 있는지 확인
        if '3' in s or '6' in s or '9' in s:
            count += 1

tsn(a, b)
print(count)