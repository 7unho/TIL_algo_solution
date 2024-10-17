"""
n := 화살 개수
result := 라이언이 가장 큰 점수 차로 이길 경우의 수
"""
from itertools import product
def solution(n, info):
    answer = [-1]
    scoreGap = 0
    for case in product((True, False), repeat = 11):
        cnt = sum([info[i] + 1 for i in range(11) if case[i]])
        
        if cnt > n: continue
        apeech = sum([10 - i for i in range(10) if info[i] > 0 and not case[i]])        
        ryan = sum([10 - i for i in range(10) if case[i]])
        
        if scoreGap < ryan - apeech:
            scoreGap = ryan - apeech
            print(scoreGap, ryan, apeech)
            answer = [info[i] + 1 if case[i] else 0 for i in range(11)]
            answer[-1] += n - cnt

    return answer

    