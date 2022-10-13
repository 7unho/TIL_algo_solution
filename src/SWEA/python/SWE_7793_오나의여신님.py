from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    graph = list()

    for i in range(N):
        graph.append(list(input().rstrip()))
        for j in range(M):
            if graph[i][j] == 'S':
                start_x, start_y = i, j
            elif graph[i][j] == 'D':
                target_x, target_y = i, j
            elif graph[i][j] == '*':
                virus_x, virus_y = i, j

    dist = [[-1] * M for _ in range(N)]


    user_queue = deque([])
    user_queue.append((start_x, start_y))

    virus_queue = deque([])
    virus_queue.append((virus_x, virus_y))

    dist[start_x][start_y] = 0
    while user_queue:
        user_x, user_y = user_queue.popleft()
        virus_x, virus_y = virus_queue.popleft()

        if user_x == target_x and user_y == target_y:
            break

        # 바이러스 확산
        for i in range(4):
            virus_nx = virus_x + dx[i]
            virus_ny = virus_y + dy[i]
            if virus_nx < 0 or virus_ny < 0 or virus_nx >= N or virus_ny >= M:
                continue

            if graph[virus_nx][virus_ny] in ['X', 'D']:
                continue

            if graph[virus_nx][virus_ny] != '*':
                graph[virus_nx][virus_ny] = '*'
                virus_queue.append((virus_nx, virus_ny))
        
        for i in range(4):
            user_nx = user_x + dx[i]
            user_ny = user_y + dy[i]

            if user_nx < 0 or user_ny < 0 or user_nx >= N or user_ny >= M:
                continue

            if graph[user_nx][user_ny] in ['*', 'X']:
                continue

            if dist[user_nx][user_ny] == -1:
                dist[user_nx][user_ny] = dist[user_x][user_y] + 1
                user_queue.append((user_nx, user_ny))
                

    answer = dist[target_x][target_y] if dist[target_x][target_y] >= 0 else 'GAME OVER'

    print(f"#{tc} {answer}")