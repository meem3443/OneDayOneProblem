### 1. 문제 이름 (Problem Name)

재귀함수의 꽃

- 개발 블로그 링크

### 2. 사용 개념 (Concepts Used)

- 재귀

### 3. 문제 이해 및 초안 (Drafting)

- N이 주어지면 재귀함수를 단 하나만 이용하여 다음과 같이 출력하는 프로그램을 작성해보세요
- N에서 1까지 1씩 감소하며 하나씩 출력했다가, 다시 1부터 N까지 1씩 증가하며 출력합니다

### 4. 로직 설계 (Logic Design)

재귀함수(정수):
if 0이하 라면:
되돌리기
정수 출력하기
재귀함수(정수-1)
정수 출력하기

### 5. 실제 코드 (Actual Code)

```
def recursionPrint(N: int):
    if N <= 0:
        return
    print(N, end=" ")
    recursionPrint(N-1)
    print(N, end=" ")
    N = int(input())
    recursionPrint(N)
```

### 6. 시행착오 (Trial & Error)

없음

### 7. 결과 및 느낀점 (Results & Reflections)

수행 시간
50ms

메모리 사용량
16MB
