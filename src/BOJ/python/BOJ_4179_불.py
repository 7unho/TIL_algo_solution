# 입력값 : R ( 행 ), C ( 열 )
#        #(벽), .(지나갈 수 있음), J(초기 위치), F(불이 난 공간)
# 출력값 : 탈출할 수 없는 경우 -> IMPOSSIBLE, 탈출 가능하다면 최단 시간

import sys
input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]

for i in range(R):
    print(graph[i])