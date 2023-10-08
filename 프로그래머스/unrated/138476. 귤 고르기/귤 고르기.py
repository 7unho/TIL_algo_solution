import heapq
def solution(k, tangerine):
    answer = 0
    items = {}
    hq = []
    for t in tangerine:
        items[t] = items.get(t, 0) + 1\
    
    for size, cnt in items.items():
        heapq.heappush(hq, (-cnt, size))
        
    while True:
        cnt, size = hq[0]
        
        if -cnt >= k: answer += 1; break
        
        k += cnt
        answer += 1
        heapq.heappop(hq)
        
    return answer