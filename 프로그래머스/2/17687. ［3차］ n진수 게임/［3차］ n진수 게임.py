"""
n := n진법
t := 출력 숫자의 개수
m := 참여자 수
p := 내 순서
"""
def convert(num, format):
    res = ''
    type = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F',
    }
    if num == 0: return '0'

    while num:
        c = str(num % format)
        if len(c) >= 2:
            c = type[c]
        res = c + res
        num //= format
        
    return res

def getWord(n, t, m, p):
    res = ''

    num = 0
    while len(res) < (t - 1) * m + p:
        res += convert(num, n)
        num += 1
    
    return res

def solution(n, t, m, p):
    answer = []
    num = 0
    # 0부터 숫자 증가하면서 문자열의 길이가 t를 넘어갈 때 까지
    word = getWord(n, t, m, p)

    for turn, w in enumerate(word):
        if len(answer) == t: break
        
        if turn % m + 1 == p:
            answer.append(w)
    return ''.join(answer)