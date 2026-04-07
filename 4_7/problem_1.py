def year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            print("false")
        else:
            print("true")

    else:
        print("false")
    
n = int(input())

year(n)