# P = 응시자
# 0 = 빈 테이블
# X = 파티션
# 거리 2이내에 응시자가 존재하지 않도록

# return 1 or 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def outOfRange(x, y):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return True
    return False

# 범위내에 사람이 존재하면 True not False
def isExist(place, x, y, direction, flag):
    for i in range(4):
        if abs(direction - i) == 2: continue
        nx = x + dx[i]
        ny = y + dy[i]
        
        if outOfRange(nx, ny): continue
        
        if place[nx][ny] == 'P' and flag == 'O':
            return True
    return False

def isValid(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] != 'P': continue
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if outOfRange(nx, ny): continue
                
                if place[nx][ny] == 'P':
                    return 0
                
                if isExist(place, nx, ny, i, place[nx][ny]):
                    return 0
                
    return 1
    
def solution(places):
    answer = []
    for place in places:
        answer.append(isValid(place))
    return answer