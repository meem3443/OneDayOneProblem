n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def hab(a1, a2):
    total = 0
    for i in range(a1 - 1, a2):
        total += arr[i]
    return total

for a1, a2 in queries:
    print(hab(a1, a2))