## 1. 힙 정렬 구현


## 2. 사용 개념 (Concepts Used)

힙 정렬, heapify

## 3. 문제 이해 및 초안 (Drafting)

힙 정렬로 n개의 숫자를 오름차순 정렬

## 4. 로직 설계 (Logic Design)

입력값 받기

n/2번째 원소부터 1번쨰 원소까지 돌며 heapify진행 

heapify : 현재 원소와 그 자식(왼,오)을 비교해서 자식이 큰 경우 교환

교환 된 위치에서 또 heapify 진행

-> max-heap 완성

n을 하나씩 줄이며 현재 최댓값(최상단 원소)과 가장 끝 노를 교

1번 노드를 기준으로 다시 heapify하며 max-heap 상태 유지 

출력

