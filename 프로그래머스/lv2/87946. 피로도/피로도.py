# k = 유저의 현재 피로도
# dungeons = [[던전 별 최소 필요 피로도, 소모 피로도]]
# answer = 최대로 탐험할 수 있는 던전 수

from itertools import permutations

def simulation(k, dungeons):
    cnt = 0
    for dungeon in dungeons:
        if k < dungeon[0]: break
    
        k -= dungeon[1]
        cnt += 1
    return cnt
        
def solution(k, dungeons):
    answer = -1
    
    for case in list(permutations(dungeons, len(dungeons))):
        answer = max(answer, simulation(k, case))
    
    return answer