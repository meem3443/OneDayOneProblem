monthPerDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeek = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
m1, d1, m2, d2 = map(int, input().split())
day = input()
TotalDay1 = 0
TotalDay2 = 0
IntergeratedTotalDay = 0

for i in range(m1-1):
    TotalDay1 = TotalDay1 + monthPerDay[i]
TotalDay1 = TotalDay1 + d1

for i in range(m2-1):
    TotalDay2 = TotalDay2 + monthPerDay[i]
TotalDay2 = TotalDay2 + d2

Weight = dayOfWeek[day]

IntergeratedTotalDay = ((TotalDay2 - TotalDay1 - Weight) //7) + 1

print(IntergeratedTotalDay)
