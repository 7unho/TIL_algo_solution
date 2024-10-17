"""
n := 화살 개수
result := 라이언이 가장 큰 점수 차로 이길 경우의 수
"""
from itertools import product
def solution(n, info):
    info.reverse()
    answer = [-1]
    maxGap = 0
    for case in product((True, False), repeat = 11):
        cnt = sum([info[i] + 1 for i in range(11) if case[i]])
        
        if cnt > n: continue
        apeech = sum([i for i in range(11) if info[i] > 0 and not case[i]])        
        ryan = sum([i for i in range(11) if case[i]])
        
        if maxGap >= ryan - apeech: continue
           
        maxGap = ryan - apeech
        answer = [info[i] + 1 if case[i] else 0 for i in range(11)]
        answer[0] += n - cnt
        
    answer.reverse()
    return answer

    