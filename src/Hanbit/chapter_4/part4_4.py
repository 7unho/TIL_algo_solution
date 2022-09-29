# 입력값 0:육지, 1:바다
# 방위 0:북, 1:동, 2:남, 3:서
# 방위 -> wayPoint # 방향 전환 -> ( wayPoint + 3 ) % 4

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

def turn_left():
    global direction
    direction = ( direction + 3 ) % 4

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = x + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count = count + 1
        turn_time = 0
        continue
    else:
        turn_time = turn_time + 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)