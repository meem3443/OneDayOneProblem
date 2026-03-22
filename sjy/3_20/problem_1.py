row = int(input())

# Please write your code here.



def pr(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print(f"{cnt}", end=" ")
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

pr(row)

