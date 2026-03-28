gender = int(input())
age = int(input())
if age >=19:
    if gender == 0:
        print("MAN(성인남자)")
    else:
        print("WOMAN(성인여자)")
else:
    if gender == 0:
        print("BOY(미성년남자)")
    else:
        print("GIRL(미성년여자)")