"""
N * M 그래프

석유(1), 빈땅(0)
answer = 시추관을 하나 뚫어서 얻을 수 있는 석유의 최댓값.

1. 석유 정보 추출
2. 시추관이 석유 범위에 있는지 확인
   -> 있다면 answer + 해당 석유 덩어리 개수 

"""
from collections import deque

N, M = 0, 0
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
groupIdx = 2
def solution(land):
    global N, M, oils, groupIdx
    answer = 0
    N, M = len(land), len(land[0])
    visited = [[-1] * M for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            if land[x][y] == 0 or visited[x][y] != -1: continue
            findOils(x, y, visited, land)
            groupIdx += 1
        
    oilCnt = getOilCnt(visited)
    for y in range(M):
        isSelected = [False] * (groupIdx - 1)
        caseSum = 0
        for x in range(N):
            if isSelected[visited[x][y] - 1]: continue
            if visited[x][y] == -1: continue
            
            isSelected[visited[x][y] - 1] = True
            caseSum += oilCnt[visited[x][y] - 1]

            answer = max(answer, caseSum)
    
    return answer

def findOils(x, y, visited, land) -> any: # 석유 덩어리 구하기
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        visited[x][y] = groupIdx
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if isNotInLand(nx, ny): continue
            if visited[nx][ny] != -1: continue
            if land[nx][ny] == 0: continue
            visited[nx][ny] = groupIdx
            q.append([nx, ny])
    
def isNotInLand(x, y):
    global N, M
    return x < 0 or y < 0 or x >= N or y >= M

def getOilCnt(visited) -> list:
    global N, M
    oilCnt = [0] * (groupIdx - 1)
    
    for x in range(N):
        for y in range(M):
            if visited[x][y] == -1: continue
            oilCnt[visited[x][y] - 1] += 1
    
    return oilCnt
