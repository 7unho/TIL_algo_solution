"""
[백준 2239] 스도쿠
https://www.acmicpc.net/problem/2239


"""
# 라이브러리 임포트
import sys
input = sys.stdin.readline

# 스도쿠
## 입력값 : 9 * 9의 스도쿠 배열
## 출력값 : 완성된 스도쿠 배열

import sys
input = sys.stdin.readline

graph = [list(map(int, input().rstrip())) for _ in range(9)]

points = []
for i in range(9):
    for j in range(9):
        if graph[i][j] != 0: continue
        points.append((i, j))

def checkRow(row, number):
    # 행 탐색
    for i in range(9):
        if graph[row][i] == number: return False
    return True

def checkCol(col, number):
    # 열 탐색
    for i in range(9):
        if graph[i][col] == number: return False
    return True

def checkArea(point, number):
    x, y = point
    # 구역 탐색
    for i in range((x // 3) * 3, (x // 3) * 3 + 3):
        for j in range((y // 3) * 3, (y // 3) * 3 + 3):
            if graph[i][j] == number: return False
    
    return True

def solution(depth):
    if depth == len(points):
        # 스도쿠가 다 채워졌다면, ( 0이 없다면 ) graph출력후 종료
        for i in range(9):
            if graph[i].count(0) != 0: return
        
        for i in range(9):
            print(''.join(list(map(str, graph[i]))))
        exit(0)
    
    # 1 ~ 9까지 숫자 대입
    for i in range(1, 10):
        if checkRow(points[depth][0], i) and checkCol(points[depth][1], i) and checkArea(points[depth], i):
            graph[points[depth][0]][points[depth][1]] = i
            solution(depth + 1)
            graph[points[depth][0]][points[depth][1]] = 0

solution(0)