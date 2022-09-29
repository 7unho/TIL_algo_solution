# 입력값 : N, ( n&n 의 맵)
# 입력값 : L, R, U, D (상하좌우)

n = int(input())
move = list(input().split())

x, y = 1, 1
boundary_x, boundary_y = n-1, n-1

for item in move:
    if item == 'U' and y > 1:
        y = y - 1
    if item == 'D' and y < boundary_y:
        y = y + 1
    if item == 'L' and X > 1:
        x = x - 1
    if item == 'R' and x < boundary_x:
        x = x + 1

print(y, x)