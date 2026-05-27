numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sor = list(filter(lambda x: x % 2 == 0, numbers))
sor2 = list(map(lambda x: x ** 2, sor))

print(sor2)