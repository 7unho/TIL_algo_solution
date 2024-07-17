"""
answer ->   1. 큐에 값이 없다면 -> [0, 0]
            2. 큐에 값이 있다면 -> [최대, 최소]

최대힙, 최소힙 두개의 변수를 선언
I -> 두개의 원소에 push
D 1 -> 최대힙에서 pop
D -1 -> 최소 힙에서 pop

모든 연산이 끝나고 최대힙과 최소힙의 공통 부분만 확인해서 최대 최소 값 추출
"""
import heapq

def solution(operations):
    answer = []
    q = list()

    for i in range(len(operations)):
        cmd, value = operations[i].split(" ")
        minHeap = q
        maxHeap = [-item for item in q]

        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)
        
        if cmd == "I":
            heapq.heappush(maxHeap, -int(value))
            heapq.heappush(minHeap, int(value))
        elif value == '-1': # 최솟값 삭제
            if not minHeap: continue
            heapq.heappop(minHeap)
        elif value == '1':
            if not maxHeap: continue
            heapq.heappop(maxHeap)

        maxHeap = [ -item for item in maxHeap]
        q = list(set(maxHeap) & set(minHeap))
    return [0, 0] if not q else [max(q), min(q)]