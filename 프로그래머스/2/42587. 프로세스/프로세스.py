from collections import deque
def is_highest(current, q):
    for i, priority in q:
        if current < priority: return False
    
    return True

def solution(priorities, location):
    answer = 0
    q = deque([[i, priority] for i, priority in enumerate(priorities)])
    
    while q:
        PID, priority = q.popleft()
        
        if not is_highest(priority, q):
            q.append([PID, priority])
            continue
        
        answer += 1
        if PID == location: break
        
    return answer