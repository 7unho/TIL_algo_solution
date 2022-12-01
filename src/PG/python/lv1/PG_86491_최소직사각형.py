# 모든 명함을 수납할 수 있는 가장 작은 크기의 지갑을 구하라.
## 1. 크기 순서로 정렬 후 경우의 수 비교하기..
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    answer = 0
    MAX_w, MAX_h = 0, 0
    for size in sizes:
        size.sort()
        MAX_w = max(MAX_w, size[0])
        MAX_h = max(MAX_h, size[1])
    
    answer = MAX_h * MAX_w
    return answer

print(solution(sizes))