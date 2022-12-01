# 가장 많은 정답을 맞힌 수포자를 출력하라
## 1번 수포자 : (1, 2, 3, 4, 5), ... -> 6 0 ? -> 1
## 2번 수포지 : 2, 1, 2, 3, 2, 4, 2, 5, ... 8n
## 3번 수포자 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ... 10n

answers = [1, 2, 3, 4, 5]
# answers = [1, 3, 2, 4, 2]

def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    cnt = [0, 0, 0, 0]
    K = len(answers)
    one *= (K // 5) + 1
    two *= (K // 8) + 1
    three *= (K // 10) + 1
    
    for i in range(K):
        if answers[i] == one[i]: cnt[1] += 1
        if answers[i] == two[i]: cnt[2] += 1
        if answers[i] == three[i]: cnt[3] += 1
    
    MAX = max(cnt)
    for i in range(1, 4):
        if MAX == cnt[i]: answer.append(i)

    return answer

print(solution(answers))
