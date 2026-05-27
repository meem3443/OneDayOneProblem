N, M = map(int, input().split())
K = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dust = set()
for _ in range(K):
    x, y = map(int, input().split())
    dust.add((x - 1, y - 1))

visited = [[False] * M for _ in range(N)]

# 후보군
candidates = [(-board[0][0], 0, 0)]

bag = []
total = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def push(heap, item):
    heap.append(item)

    i = len(heap) - 1

    while i > 0:
        p = (i - 1) // 2

        if heap[p] <= heap[i]:
            break

        heap[p], heap[i] = heap[i], heap[p]
        i = p


def pop(heap):
    root = heap[0]

    last = heap.pop()

    if heap:
        heap[0] = last

        i = 0

        while True:
            l = i * 2 + 1
            r = i * 2 + 2
            smallest = i

            if l < len(heap) and heap[l] < heap[smallest]:
                smallest = l

            if r < len(heap) and heap[r] < heap[smallest]:
                smallest = r

            if smallest == i:
                break

            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest

    return root


while candidates:
    neg_c, x, y = pop(candidates)

    if visited[x][y]:
        continue

    visited[x][y] = True

    c = -neg_c

    # 꽃 획득
    total += c
    push(bag, -c)

    # 꽃가루 구역이면 가장 큰 꽃 제거
    if (x, y) in dust:
        removed = -pop(bag)
        total -= removed

    # 인접 칸 추가
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                push(candidates, (-board[nx][ny], nx, ny))

print(total)