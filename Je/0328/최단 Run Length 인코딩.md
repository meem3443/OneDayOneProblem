## [최단 Run Length 인코딩] 분석

* **입력**: 길이 N 문자열
* **출력**: shift를 진행하여 나올 수 있는 Run-Length Encoding 이후의 결과들 중 최소 길이

### 제약
* **시간**: 1000ms  
* **메모리**: 80MiB

### 알고리즘
* 배열 끝에서부터 거꾸로 문자가 바뀌는 지점 찾기
  > O(N)
* 바뀌는 지점까지 shift진행
  > O(N)
* Run-Length Encoding 진행 후 글자 길이 구하기
  > O(N)
* 총 시간복잡도 O(N)

  
### 엣지 케이스 (Edge Cases) & 예외 처리
* 첫 문자 != 마지막 문자: 바로 Run-Length Encoding 진행
* Run-Length Encoding 진행시 길이는 문자 + 횟수(최대10)
  

### 로직 설계 
1. 문자 입력 받기
2. 문자열을 거꾸로 순회하며 A[i] != A[i-1] 지점 탐색
3. 해당 지점까지 shift
   > A[i:] + A[:i]
4. 3 결과를 순회하며 문자가 같다면 count +1, 다르다면 새 문자열에 문자+count를 더한 후 count =1
5. 출력
