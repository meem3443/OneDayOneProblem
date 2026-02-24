# 1. 입력값을 통해서 오름차순으로 값을 정렬시킨후 배열에 저장한다.
# 2. 정렬된 배열의 맨앞과, 맨뒤를 더하여 새로운 배열에 저장한다. (여러 원소들의 조합들을 모아놓은 배열중 가장 작은 값 도츨을 위해)
# 3. 해당 배열에서 가장 작은 값을 출력한다.

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = []
for i in range(len(nums)):
    result.append(nums[i] + nums[-(i+1)]) 
result.sort(reverse=True)
print(result)