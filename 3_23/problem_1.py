n = int(input())

# Please write your code here.

def numi(x):

    new = str(x)
    global add
    add = 0
    for i in range(len(new)):
        add += int(new[i])
    return add


numi(n)

if n % 2 == 0 and add % 5 == 0:
        print("Yes")
else:
        print("No")