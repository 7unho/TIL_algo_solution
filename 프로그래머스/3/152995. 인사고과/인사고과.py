def solution(scores):
    answer = 1
    wanho = scores[0] + [sum(scores[0])]

    scores.sort(key=lambda x: (-x[0], x[1]))
    max_b = 0

    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        
        if b >= max_b:
            max_b = b

            if a + b > wanho[2]:
                answer += 1

    return answer