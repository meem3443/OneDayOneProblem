## 1. 선택 정렬 구현


## 2. 사용 개념 (Concepts Used)

선택 정렬

## 3. 문제 이해 및 초안 (Drafting)

선택 정렬로 n개의 숫자를 오름차순 정렬

-> 탐색하며 가장 작은 값 찾고 앞에 배치 반복

-> minimum 갱신 

## 4. 로직 설계 (Logic Design)

입력값 받기

배열 맨 앞자리 minimum 설정하고 탐색하면서 비교

-> arr[minimum]보다 작은 값 발견하면 갱신하고 이어서 비교 진행

arr[i] <-> arr[minimum]

n-1번 반복

출력



