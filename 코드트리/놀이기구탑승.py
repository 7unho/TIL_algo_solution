"""
n := 격자 크기 (1 ~ N)
students := {학생번호: [선호학생번호]}

탑승 칸 조건 (비어있는 칸으로만ㅇ ㅣ동)

1. 4방향 인접 중, 좋아하는 친구의 수가 가장 많은 위치
2. 1번이 여러 개인 경우, 비어있는 칸이 가장 많은 위치, 격자 범위 내에서
3. 행 번호가 가장 작은 위치
4. 열 번호가 가장 작은 위치
for sum in r + c
    for c = sum - r

최종 점수 -> 각 학생의 점수를 합한 총 점수
좋아하는 친구의수 0: 0, 1: 1, 2:10, 3: 100, 4:1000
"""
import heapq

n = int(input())
students = dict()
seat = [[-1] * n for _ in range(n)]
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
score = [0, 1, 10, 100, 1000]
answer = [0] * n ** 2

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def isFull(x, y):
    return seat[x][y] != -1

def findLikes(x, y, likes):
    result = 0

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if outOfRange(nx, ny): continue
        if seat[nx][ny] not in likes: continue
        result += 1

    return result

def findEmpty(x, y):
    result = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if outOfRange(nx, ny): continue
        if isFull(nx, ny): continue
        result += 1

    return result

for _ in range(n ** 2):
    info = list(map(int, input().split()))
    # 착석좌표, 선호학생리스트
    students[info.pop(0)] = [(-1, -1), info]

for student, (point, likes) in students.items():
    available = list()

    for x in range(n):
        for y in range(n):
            if isFull(x, y): continue
            print(x, y)
            like_count = findLikes(x, y, likes)
            empty_count = findEmpty(x, y)
            heapq.heappush(available, (-like_count, -empty_count, x, y))
    
    like_count, empty_count, x, y = heapq.heappop(available)
    students[student][0] = (x, y)
    seat[x][y] = student

for student, (point, likes) in students.items():
    answer[student - 1] = score[findLikes(point[0], point[1], likes)]

print(sum(answer))