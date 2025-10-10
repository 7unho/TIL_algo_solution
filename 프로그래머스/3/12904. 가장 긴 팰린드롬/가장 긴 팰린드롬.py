def solution(word):
    global n
    n = len(word)

    for answer in range(n, 0, -1):
        for start in range(n - answer + 1):
            s, e = start, start + answer - 1
            isValid = True
            while s < e:
                if word[s] == word[e]:
                    s += 1
                    e -= 1
                else:
                    isValid = False
                    break  
            if isValid:
                return answer
    return 1