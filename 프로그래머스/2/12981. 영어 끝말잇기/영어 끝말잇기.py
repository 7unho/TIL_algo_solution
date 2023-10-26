def solution(n, words):
    answer = [0, 0]

    turn = 0
    isUsed = set([words[0]])
    for i in range(1, len(words)):
        if words[i] in isUsed or words[i - 1][-1] != words[i][0]:
            answer = [(i % n) + 1, i // n + 1]
            break
        isUsed.add(words[i])

    return answer