ASC = 0
DESC = 1
x_sign = [1, -1]
y_sign = [1, -1]

def solution(points, routes):
    answer = 0
    crashes = dict()
    X = len(routes)
    for i in range(X):
        start = routes[i][0]
        targets = routes[i][1:]
        time = 0
        sx, sy = points[start - 1]
        crashes[(sx, sy, time)] = crashes.get((sx, sy, time), 0) + 1
        for target in targets:
            ex, ey = points[target - 1]
            
            dx = x_sign[ASC] if sx < ex else x_sign[DESC]
            dy = y_sign[ASC] if sy < ey else y_sign[DESC]

    
            for _ in range(abs(sx - ex)):
                nx = sx + dx
                time += 1
                crashes[(nx, sy, time)] = crashes.get((nx, sy, time), 0) + 1
                sx = nx
                
            for _ in range(abs(sy - ey)):
                ny = sy + dy
                time += 1
                crashes[(sx, ny, time)] = crashes.get((sx, ny, time), 0) + 1
                sy = ny
                    
            start = target
    
    for k, count in crashes.items():
        if count >= 2: 
            answer += 1
            
    return answer