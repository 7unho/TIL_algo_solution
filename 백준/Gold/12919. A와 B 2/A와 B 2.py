S = input()
T = input()
answer = 0

def isMatched(keyword):
    global answer

    if len(keyword) < len(S):
        return
    
    if keyword == S:
        answer = 1
        return
    
    # 첫번째 문자가 B라면, B를 없애고 reverse
    if keyword[0] == 'B':
        nKeyword = keyword[::-1][:-1]
        isMatched(nKeyword)

    if keyword[-1] == 'A':
        nKeyword = keyword[:-1]
        isMatched(nKeyword)

isMatched(T)

print(answer)


"""
next := prev + 'A', reversed(prev + 'B')
prev := next - 'A', reversed(next) - 'B'
"""