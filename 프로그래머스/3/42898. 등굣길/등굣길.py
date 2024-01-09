"""
n * m 배열
puddles = 웅덩이 있는 곳

오른쪽과 아래쪽으로만 이동

answer = answer % 1_000_000_007
"""
LEFT, TOP = 0, 1
def init(n, m, puddles):
    dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
    graph = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = [1, 1]
    for puddle in puddles:
        c, r = map(lambda x: (x - 1), puddle)
        
        graph[r][c] = -1
        
    return dp, graph

def isPuddle(x, y, graph):
    return graph[x][y] == -1

def solution(m, n, puddles):
    dp, graph = init(n, m, puddles)
    for x in range(1, n):
        if isPuddle(x, 0, graph): continue
            
        dp[x][0][TOP] += dp[x - 1][0][TOP]
        
    for y in range(1, m):
        if isPuddle(0, y, graph): continue
            
        dp[0][y][LEFT] += dp[0][y - 1][LEFT]
    
    for x in range(1, n):
        for y in range(1, m):
            if isPuddle(x, y, graph): continue
            
            # 위 방향이 물웅덩이가 아닐 경우
            if not isPuddle(x - 1, y, graph):
                dp[x][y][TOP] += (dp[x - 1][y][TOP] + dp[x - 1][y][LEFT])
                
            # 왼쪽 방향이 물웅덩이가 아닐 경우
            if not isPuddle(x, y - 1, graph):
                dp[x][y][LEFT] += (dp[x][y - 1][LEFT] + dp[x][y - 1][TOP])
    return sum(dp[n - 1][m - 1]) % 1_000_000_007
# print(solution(4, 3, [[1, 2], [1, 3]]))