x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

inter_x1 = max(x1[0], x1[1]) 
inter_x2 = min(x2[0], x2[1]) 
inter_y1 = max(y1[0], y1[1]) 
inter_y2 = min(y2[0], y2[1])

inter_width = max(0, inter_x2 - inter_x1)
inter_height = max(0, inter_y2 - inter_y1)
inter_area = inter_width * inter_height

# 2. A의 원래 가로, 세로
width_a = x2[0] - x1[0]
height_a = y2[0] - y1[0]
area_a = width_a * height_a

is_width_full = (inter_width == width_a)   # 가로를 꽉 채웠나?
is_height_full = (inter_height == height_a) # 세로를 꽉 채웠나?

# 가로가 꽉 찼고(width 일치) AND (아랫변이 닿았거나 OR 윗변이 닿았거나)
if is_width_full and (inter_y1 == y1[0] or inter_y2 == y2[0]):
    print(area_a - inter_area)

# 세로가 꽉 찼고(height 일치) AND (왼쪽변이 닿았거나 OR 오른쪽변이 닿았거나)
elif is_height_full and (inter_x1 == x1[0] or inter_x2 == x2[0]):
    print(area_a - inter_area)

# 그 외 (귀퉁이만 겹침, 중간만 뚫림, 안 겹침) -> 원래 넓이 그대로
else:
    print(area_a)

