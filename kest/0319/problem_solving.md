## 1. 황금비율 토스트


## 2. 사용 개념 (Concepts Used)

Iterator , linked list

## 3. 문제 이해 및 초안 (Drafting)

L : 앞
R : 뒤
D : 뒤에꺼 삭제
P & : &문자 추가

## 4. 로직 설계 (Logic Design)

입력값 받기 

리스트, iterator 생성

4가지 경우 쪼개기

출력

## 5. 시행착오 (Trial & Error)
시간초과 발생 -

Scanner → BufferedReader

System.out.print → StringBuilder

3082ms / 188MB → 129ms / 10MB

## 6. 결과 및 느낀점 (Results & Reflections)

else if(command.startsWith("P ")){
char ch = command.charAt(2); 
->startsWith 처음 봄 

