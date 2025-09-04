"""
genres := 노래의 장르
plays := 재생횟수
answer := 노래의 고유 번호

장르 : heapq(재생횟수 desc, 고유번호 asc)

"""
import heapq

def solution(genres, plays):
    answer = []
    n = len(plays)
    scores = dict()
    rank = dict()
    
    for song in range(n):
        if not scores.__contains__(genres[song]):
            scores[f"{genres[song]}"] = list()
            rank[f"{genres[song]}"] = 0
        
        heapq.heappush(scores[f"{genres[song]}"], (-plays[song], song))
        rank[f"{genres[song]}"] += plays[song]
        
    
    for genre in sorted(rank.keys(), key=lambda x: rank[x], reverse=True):
        for _ in range(min(2, len(scores[genre]))):
            answer.append(heapq.heappop(scores[genre])[1])
            
    return answer