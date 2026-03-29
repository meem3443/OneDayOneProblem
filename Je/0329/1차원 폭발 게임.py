n, m = map(int, input().split())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.


# 배열을 순회하며 연속된 숫자 카운트, m이상일 경우 새 배열에 추가하지 않음(is_boom = True)
# 위 과정을 is_boom == False가 될 때까지 반복


arr =blocks
while True:
    is_boom =False
    if not arr:
        break
    n_arr = []
    count = 1
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:          #연속X
            if(count >= m):
                is_boom =True
            else:
               n_arr += [arr[i-1]] * count
            count = 1
        else:
            count +=1
    if(count >= m):
        is_boom =True
    else:
        n_arr += [arr[-1]] * count

    arr= n_arr
    if is_boom ==False:
        break

print(len(arr))

for row in arr:
    print (row)

    
