# 재귀함수(정수, 결과값):
# if 정수 == 0:
# return 결과값
# 재귀함수(정수 / 10, 결과값)
# 결과값 = 결과값 + 정수^2

def recursionSum(N: int, result: int):
    if N == 0:
        return result
    return recursionSum(N // 10, result + (N % 10)**2)


N = int(input())
print(recursionSum(N, 0))

