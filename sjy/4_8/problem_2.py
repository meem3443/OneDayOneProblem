a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def summation(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def dvision(x, y):
    return x // y

if o == "+":
    k = summation(a, c)
    print(f"{a} + {c} = {k}")

elif o == "-":
    k = minus(a, c)
    print(f"{a} - {c} = {k}")

elif o == "*":
    k = multiple(a, c)
    print(f"{a} * {c} = {k}")

elif o == "/":
    k = dvision(a, c)
    print(f"{a} / {c} = {k}")

else:
    print("False")

