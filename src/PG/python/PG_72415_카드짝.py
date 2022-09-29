import math
import queue

Board = []
# 모든 카드
Allcard = {}

# 모든 카드가 제거되었는지 확인용 변수 ( 비트 마스킹 )
## 0번째 비트 = 1,
## 0번째 비트 : 보드에서 숫자가 없는 빈 칸으로, 삭제되었다고 가정함.
Allremoved = 1

# 최소 조작 횟수
MinCnt = math.inf

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 제거된 카드상태, 시작 위치, 목적지를 매개변수로 받아 최단거리 산출
def bfs(removed, cursor, distance):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = queue.Queue()
    q.put(cursor)
    
    while q:
        current = q.get()

        # 현재 위치가 목적지와 같다면
        if current[0] == distance[0] and current[1] == distance[1]:
            return current[2]
        
        for i in range(4):
            nx = current[0] + dx[i]
            ny = current[1] + dy[i]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.put((nx, ny, current[2] + 1))

            # 맵 범위가 4이므로 컨트롤을 눌러봤자 현재 이동한 위치에서 2번 더 이동할 수 있기에 범위를 2로 지정
            for j in range(2):
                # 지금 위치에 카드가 존재하는 경우
                if removed & (1 << Board[nx][ny]) == 0:
                    break

                if nx + dx[i] < 0 or nx + dx[i] >= 4 or ny + dy[i] < 0 or ny + dy[i] >= 4:
                    break

                nx += dx[i]
                ny += dy[i]
                
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.put((nx, ny, current[2] + 1))

    return math.inf


# 현재까지의 조작 횟수, 현재 까지의 삭제된 카드( 비트 형태 ), 현재 커서의 위치
def permutate(cnt, removed, cursor):
    global MinCnt

    # 종료조건
    if cnt >= MinCnt:
        return

    if removed == Allremoved:
        MinCnt = min(MinCnt, cnt)
        return
    
    for num, card in Allcard.items():
        # num이 이미 삭제되었다면 스킵
        if removed & 1 << num:
            continue

        # 순차로 카드를 제거하기 위한 과정
        ## (현재 커서부터 첫번째 카드까지, 첫 번째 카드부터 2번째 카드까지, 엔터 2번)의 합이 조작 횟수
        order = bfs(removed, cursor, card[0]) + bfs(removed, card[0], card[1]) + 2

        # 역순으로 카드를 제거하기 위한 과정
        ## (현재 커서부터 첫번째 카드까지, 첫 번째 카드부터 2번째 카드까지, 엔터 2번)의 합이 조작 횟수
        reverse = bfs(removed, cursor, card[1]) + bfs(removed, card[1], card[0]) + 2

        # 재귀 호출
        ## 순차 카드 제거
        ### 마지막 좌표(커서)가 card1에 가있으므로, card1에 커서
        permutate(cnt + order, removed | 1 << num, card[1])

        ## 역순 카드 제거
        ### 마지막 좌표(커서)가 card0에 가있으므로, card0에 커서
        permutate(cnt + reverse, removed | 1 << num, card[0])
        

def solution(board, r, c):
    global Board, Allcard, Allremoved

    Board = board
    
    # 2중 포문이 끝나면
    ## 각 그림판의 모든 카드가 Allcard에 들어가고,
    ## 모든 카드의 숫자에 해당하는 비트가 1로 설정되게 한다.
    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            # 보드에 있는 값이 0이 아니라면
            if num:
                # 1을 숫자만큼 왼쪽 시프트해서 or연산
                ## 보드의 숫자(num)이 1이면 1만큼 비트연산 후 or연산한 값을 넣어줌.
                Allremoved |= 1 << num
                if num in Allcard:
                    Allcard[num].append((i, j, 0))
                else:
                    # Allcard에 num이 없다면
                    # 해당 num키의 현재 좌표와 조작횟수를 넣어준다.
                    Allcard[num] = [(i, j, 0)]
        
    # 조작횟수 : 0, 삭제된 카드 비트 : 0이므로 1, 현재 커서 : 입력받은 커서 좌표
    permutate(0, 1, (r, c, 0))
    return MinCnt