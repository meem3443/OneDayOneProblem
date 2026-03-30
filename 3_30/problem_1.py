a = ["L","E","B","R","O","S","C","O","D","E"]
a.reverse()
print(''.join(a))

# 내가 몰랐던 답
arr = list(input().split())


for i in range(9, -1, -1):
	print(arr[i], end="")