from collections import deque

def solution(priorities, location):
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    order = 0  # 실행 순서

    while queue:
        current = queue.popleft()

        # 현재 프로세스보다 높은 우선순위가 있는지 확인
        if any(current[0] < other[0] for other in queue):
            queue.append(current)  # 다시 큐에 넣기
        else:
            order += 1  # 실행된 순서 증가
            if current[1] == location:
                return order  # 목표한 프로세스 실행됨