dx = {
    'U': -1,
    'D': 1,
    'L': 0,
    'R': 0
}

dy = {
    'U': 0,
    'D': 0,
    'L': -1,
    'R': 1
}
def IsOutOfRange(x, y) -> bool:
    return x < 0 or y < 0 or x >= 11 or y >= 11

def isKnownRoad(graph, x, y, nx, ny):
    return graph[x][y][(nx, ny)] != 0

def solution(dirs):
    answer = len(dirs)
    
    graph = [[{
        (i - 1, j): 0,
        (i + 1, j): 0,
        (i, j - 1): 0,
        (i, j + 1): 0
    } for j in range(11)] for i in range(11)]
    x, y = 5, 5

    for dir in dirs:
        nx, ny = x + dx[dir], y + dy[dir]
        if IsOutOfRange(nx, ny): 
            answer -= 1
            continue
        if isKnownRoad(graph, x, y, nx, ny):
            answer -= 1
        graph[nx][ny][(x, y)] += 1
        graph[x][y][(nx, ny)] += 1
        
        x = nx
        y = ny
    
    return answer