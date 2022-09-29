# 입력값 : 트럭에 실을 수 있는 최대 무게 (M),  load = 물건 리스트
# 출력값 : 모둔 물건을 운반하기 위해 필요한 트럭 수의 최솟값, 물건 운반 x -> -1리턴

from importlib.machinery import FrozenImporter
import sys
input = sys.stdin.readline

M = 9
load = [2, 2, 3, 3, 3, 5]
load.sort(reverse=True)
print(load)

answer = 0

if max(load) > M :
    answer = -1
else:
    while True:
        if not load:
            break

        temp = 0
        idxs = []
        for i in range(len(load)):
            if temp + load[i] <= M:
                temp += load[i]
                idxs.append(load[i])
                
        for i in range(len(idxs)):
            load.remove(idxs[i])

        answer += 1
print(answer)