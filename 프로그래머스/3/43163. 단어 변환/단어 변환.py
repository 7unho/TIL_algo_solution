from collections import deque
"""
PS : begin -> target 최단 변환 과정
[rules]
1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
2. words에 있는 단어로만 변환 가능
"""

def contains(word, target) -> bool: # 치환 여부 검증
    cnt = 0
    
    for i in range(len(word)):
        if word[i] != target[i]: cnt += 1
    return True if cnt <= 1 else False

def solution(begin, target, words):
    INF = int(1e9)
    answer = INF
    visited = {begin:False}
    
    for word in words:
        visited[f"{word}"] = False
            
    q = deque()
    q.append([begin, 0])
    
    while q:
        word, cnt = q.popleft()
        visited[f"{word}"] = True
        
        if word == target:
            answer = min(answer, cnt)
            break
        
        for nw in words:
            if not contains(word, nw): continue # 치환 여부 검증
            if visited[f"{nw}"]: continue
            q.append([nw, cnt + 1])
    
    
    return answer if answer != INF else 0