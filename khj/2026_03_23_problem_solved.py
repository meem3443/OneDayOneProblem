"""
1.문제 독해
A,B 두 자연수를 입력받아 A부터 B까지 짝수의 합을 구해 출력하는 프로그램.
A와 B 사이에 짝수 끼리만 list에 넣어서 합친다. 

2.논리 및 수학적 설계

a,b를 map(int, input())으로 받는다.

for num in range(a, b+1)를 한뒤
if num % 2 == 0 을 통해서 짝수를 모은다음에
append를 통해서 리스트안에  짝수들을 추가한다.

짝수 내에 있는 숫자들을 sum을 통해서 합한뒤 출력

3. 필요한 데이터 타입
정수형 데이터가 필요하다. 
for 문과 for 문 안에 if문을 통해 짝수를 선별하기.

4.
입력: a,b 입력받기
처리: for문으로 a, b까지 반복하게 만듬. 그동안 if문을 통해서 짝수 판별
짝수 append를 통해 리스트 추가.
sum 통해서 리스트 내 짝수 다 합치기.
출력: 언패킹 연산자 통해 결과 출력

"""
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
number_List = []
for num in range(a, b+1):
    if num % 2 == 0:
        number_List.append(num)

total = sum(number_List)
print(total)