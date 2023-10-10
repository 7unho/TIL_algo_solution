"""
[삼성 역테 기출] 2048 Easy 
https://www.acmicpc.net/problem/12100

N := N * N의 보드 판
graph := 보드 정보

최대 5번 이동 후, 만들 수 있는 가장 큰 블록의 값 출력
"""
# 라이브러리 임포트
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def solution(depth, board) -> any:
    global answer

    if depth >= 5: return
    
    for dir in range(4):
        nBoard = doPlay(board[:], dir)
        answer = max(answer, getMaxBlock(nBoard))

        solution(depth + 1, nBoard)
    

def getMaxBlock(board) -> int: # 보드의 가장 큰 값 리턴
    res = -1
    for i in range(N):
        for j in range(N):
            res = max(res, board[i][j])

    return res

def doPlay(board, dir) -> list: # 방향으로 이동
    nBoard = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        stack = deque()
        
        last = (-1, (-1, -1))
        for j in range(N):
            cur = board[i][j] # 좌
            nx, ny = i, j

            if dir == 1: nx, ny = j, i # 상
            elif dir == 2: nx, ny = i, N - 1 - j# 우
            elif dir == 3: nx, ny = N - 1 -j, i # 하

            cur = board[nx][ny]
            if cur == 0: continue # 빈 칸이라면,

            if last[0] != cur:
                stack.append([cur, (nx, ny)])
                last = [cur, (nx, ny)]
                continue
            
            stack[-1][0] *= 2
            last = (-1, (-1, -1))

        for k in range(len(stack)):
            if dir == 0: nBoard[i][k] = stack[k][0]
            elif dir == 1: nBoard[k][i] = stack[k][0]
            elif dir == 2: nBoard[i][N - 1 - k] = stack[k][0]
            else: nBoard[N - 1 - k][i] = stack[k][0]
    
    return nBoard

answer = getMaxBlock(board)
solution(0, board)
print(answer)