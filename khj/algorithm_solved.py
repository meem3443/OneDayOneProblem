#흙기둥 높이 맞추기?
#n개의 흙기둥이 일렬로 세워짐.
#물총을 이용해 흙기둥의 높이를 다 맞춰놓으려고 함.
#물총을 한번 쏠때마다 특정 흙기둥 1개의 높이를 정확히 1만큼 낮출 수 있음. (0 이하 안됨)
#모든 흙기둥의 높이를 동일하게 만들기 위해 물총을 쏴야 하는 최소 횟수를 구하기.

soil_n = int(input()) # 흙기둥 갯수
soil_tower = list(map(int, input().split()))[:soil_n] #흙기둥 리스트화(n개까지 받기)

minimum_H = min(soil_tower) # 흙기둥 중 최솟값 찾기

result = 0 #결괏값

for i in range(soil_n): #n회 동안 실행
    watergun = soil_tower[i] - minimum_H #흙기둥 i번째에 있는 걸 최솟값에 뺌 ==> **이게 물총 횟수임**

    result += watergun #이걸 result에 더함

print(result) # result에 출력

