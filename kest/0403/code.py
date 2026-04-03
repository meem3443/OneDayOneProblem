Y, M, D = map(int, input().split())

def yun(Y) :
    if ((Y % 4 == 0) and (Y%100==0) and (Y%400==0))  :
        return True
    elif (Y%4==0) and (Y%100==0) :
        return False
    elif (Y%4==0) :
        return True
    else :
        return False

def md(Y,M,D) :
    if yun(Y) :
        if M==2 :
            if D >29 :
                return False
            else :
                return True
    if M in [1,3,5,7,8,10,12] :
        if D >31 :
            return False
    if M in [4,6,9,11] :
        if D > 30 :
            return False
    if M==2 :
        if D > 28 :
            return False
    return True


if md(Y,M,D) :
    if M in [3,4,5] :
        print("Spring")
    elif M in [6,7,8] :
        print("Summer")
    elif M in [9,10,11] :
        print("Fall")
    elif M in [12,1,2] :
        print("Winter")

else :
    print (-1)