sen1, sen2 = input().split()

if len(sen1) < len(sen2):
    print(sen2, len(sen2), end = " ")
elif len(sen1) > len(sen2):
    print(sen1, len(sen1), end = " ")
else:
    print("same")