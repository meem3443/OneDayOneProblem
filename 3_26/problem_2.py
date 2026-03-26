A_math, A_english = map(int,input().split())
B_math, B_english = map(int,input().split())
if A_math > B_math and A_english > B_english:
    print(1)
else:
    print(0)