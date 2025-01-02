def solution(sizes):
    answer = 0
    MAX_w, MAX_h = 0, 0
    for size in sizes:
        size.sort()
        MAX_w = max(MAX_w, size[0])
        MAX_h = max(MAX_h, size[1])
    
    answer = MAX_h * MAX_w
    return answer