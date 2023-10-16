from collections import deque
"""
1. 그래프 랑 각 좌표 뻥튀기 2배씩. -> 'ㄷ' 자의 경우에 반례 생기기 때문
2. 사각형들 순회하면서 각 4좌표가 다른 사각형에 속하는지 검증
    2-1. 다른 좌표에 속하지 않는다면 graph[x][y] = 1
    
"""    
def isVertex(x, y, num, rectangle) -> bool: # 꼭짓점인지 := 다른 사각형 내부에 속하지 않는지.
    for i in range(len(rectangle)):
        cx1, cy1, cx2, cy2 = rectangle[i]
        if i == num: continue # 자기 자신은 제외
        
        if cx1 < x < cx2 and cy1 < y < cy2: return False
    return True

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0 for _ in range(101)] for _ in range(101)]
    visited = [[-1 for _ in range(101)] for _ in range(101)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    rectangle = [list(map(lambda x: x * 2, r)) for r in rectangle]
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    for i in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[i]
        # 수평 좌표 검증
        for nx in range(x1, x2 + 1):
            for ny in (y1, y2):
                if not isVertex(nx, ny, i, rectangle): continue
                graph[nx][ny] = 1

        # 수직 좌표 검증
        for ny in range(y1, y2 + 1):
            for nx in (x1, x2):
                if not isVertex(nx, ny, i, rectangle): continue
                graph[nx][ny] = 1
    
    q = deque()
    q.append((characterX, characterY))
    visited[characterX][characterY] = 0
    while q:
        x, y = q.popleft()
        
        if (x, y) == (itemX, itemY): break
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= 101 or ny >= 101: continue
            if visited[nx][ny] != -1 or graph[nx][ny] == 0: continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return visited[itemX][itemY] // 2