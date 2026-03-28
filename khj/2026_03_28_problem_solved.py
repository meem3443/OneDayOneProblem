"""
1.문제 독해
오래된 다이얼 전화기.
0을 기준으로 1은 2초 2는 3초 4는 4초...
즉 예를 들어 4번을 기준으로 5번은 1초 3번은 -1초임.

1번은 X
2번은 ABC
3번은 DEF...
어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 건다. 그럼 그 숫자에 맞는 시간 초를 계산해야한다.
특정 알파벳에 해당하는 다이얼을 걸기 위해서 필요한 최소 시간 구하기


2.논리 및 수학적 설계
list() 를 통해서 입력받은 알파벳들을 쪼개어 저장.
for 문을 통해서 조건문을 반복한다.
if ~ in 을 통해서 ABC, EDF, GHI 각각에 속하는지 검사.



3. 필요한 데이터 타입
문자열(str) 타입 필요.
딕셔너리를 통해서 abc: 3초 def: 4초 이런식으로 키 지정.
for문 통해서 abc , def 검사


4.
입력: 문자 입력 리스트에 쪼개어 추가
처리: list에 들어온 문자 만큼 반복하기.
dic의 key들을 불러오기. ('abc':1) 이라면 abc를 불러옴.
i에는 ABC, DEF, GHI, 이런식으로 들어감.
words[] 에 i가 포함하는 그 키에 value 를 result 에 더한 값을 출력ㄴ


출력: words 갯수에 따라 시간을 체크한것들을 result에 더해 result를 출력
"""
result = 0

dic = {
    "ABC":3, "DEF":4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8 , 'TUV':9, 'WXYZ':10
}
words = list(input())

for j in range(0, len(words)):

    for i in dic.keys():
        
        if words[j] in i:

            result += dic.get(i)  #dic[i]

            
print(result) 