"""
answer = 쿼리에 해당하는 조건을 만족하는 사람이 몇 명인지
"""
from collections import defaultdict
from bisect import bisect_left

scoresMap = defaultdict(list)

def buildKey(index, prefix, tokens, score): # 가능한 해시테이블의 키 생성
    if index == len(tokens) - 1:
        scoresMap[f"{prefix}"].append(score)
        return
    
    buildKey(index + 1, prefix + '-', tokens, score)
    buildKey(index + 1, prefix + tokens[index], tokens, score)

def buildScoresMap(info) -> any: # 해쉬테이블 생성
    for item in info:
        item = item.split(' ')
        tokens = item[:5]
        score = int(item[-1])
        
        buildKey(0, "", tokens, score)
    
    for k in scoresMap.keys():
        scoresMap[k].sort()

def solution(info, query):
    answer = []
    
    buildScoresMap(info)
    for q in query:
        key, condition = ''.join(q.split(' and ')).split(' ')
        
        answer.append(len(scoresMap[key]) - bisect_left(scoresMap[key], int(condition)))
    return answer