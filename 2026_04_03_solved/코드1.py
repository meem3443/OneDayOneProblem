list = ["apple", "banana", "grape", "blueberry", "orange"]

src = input()
count = 0

for p in list:
    if p[2] == src or p[3] == src:
        print(p)
        count += 1
print(count)