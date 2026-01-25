# 1. 1월 ~ 12월까지 월별 일자를 배열로 선언하기
# 2. m1, m2를 각각 m1-1, m2-1 만큼 더해서 일수 구하기
# 3. d1, d2를 각각에 더해주어 각각의 (x,y)총일수 구해주기
# 4. abs(x-y) % 7 만큼 dayOfWeek에서 전진시키기

# m1, d1, m2, d2 = map(int, input().split())

# temp = abs(m2-m1)
# i = min(m1, m2)

# for i in range(temp):
#     result = result + monthPerDay[i]
# result = (result + d2 - d1) % 7 #앞인지 뒤인지 구분없음 틀린코드
monthPerDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1, d1, m2, d2 = map(int, input().split())

mdTotal1 = 0
mdTotal2 = 0
for i in range(m1-1):
    mdTotal1 = mdTotal1 + monthPerDay[i]
mdTotal1 = mdTotal1 + d1

for i in range(m2-1):
    mdTotal2 = mdTotal2 + monthPerDay[i]
mdTotal2 = mdTotal2 + d2

result = (mdTotal2 - mdTotal1) % 7
print(dayOfWeek[0 + result])
