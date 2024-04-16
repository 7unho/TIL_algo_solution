from collections import deque
"""
bridge_length := 다리에 올라갈 수 있는 트럭 수, 다리 통과 소요 시간
weight        := 버틸 수 있는 중량
truck_weights := 트럭의 무게
return        := 모든 트럭이 다리를 건너는 최소 시간
"""
def move(closedTrucks, currentTime, bridge_length, bridge):
    truck, time = bridge[0]
    if currentTime - time >= bridge_length:
        bridge.popleft()
        closedTrucks.append(truck)
        
    
def isOver(closedTrucks, N) -> bool:
    return len(closedTrucks) == N

def isTruckEnterable(bridge, truck, bridge_length, weight):
    if truck == -1: return False
    if len(bridge) > bridge_length: return False
    if sum(map(lambda x:x[0], bridge)) + truck > weight: return False
    
    return True

def solution(bridge_length, weight, truck_weights):
    answer = 0
    N = len(truck_weights)
    
    trucks = deque(truck_weights)
    bridge = deque([])
    closedTrucks = list()
    
    while True:
        if isOver(closedTrucks, N): break
        if bridge: move(closedTrucks, answer, bridge_length, bridge)
        truck = trucks[0] if trucks else -1
        
        # 트럭이 다리에 진입 가능하다면, 다리에 진입
        if isTruckEnterable(bridge, truck, bridge_length, weight):
            trucks.popleft()
            bridge.append((truck, answer))
        

        answer += 1
        
        
    
    return answer