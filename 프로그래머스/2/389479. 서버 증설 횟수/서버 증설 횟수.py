"""
m := 서버 증설이 필요한 인원  n * m <= target < (n + 1) * m
k := 서버유지기간
servers = (서버 대수, 끝나는 시각)
answer := 최소 서버 증설 횟수
"""
def solution(players, m, k):
    answer = 0
    servers = [0 for _ in range(24)]
    
    for hour, player in enumerate(players):
        requiredServerCount = (player // m) - servers[hour]
        if requiredServerCount <= 0: continue
        
        answer += requiredServerCount
        for i in range(k):
            if hour + i >= 24: break
            servers[hour + i] += requiredServerCount
        
    return answer