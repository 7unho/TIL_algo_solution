# 1. 1부터 s까지 자를 문자열의 길이 설정
# 2. 설정된 길이만큼 문자열을 잘라 낸 리스트 생성
# 3. 문자열을 비교하며 리스트의 배열을 하나의 문자열로 압축
# 4. 1~3 과정으로 압축된 문자열 중 가장 짧은 길이 반환
def compress(tokens):
    last = ''
    cnt = 0
    res = ''
    
    for token in tokens:
        if token == last:
            cnt += 1
        else:
            if cnt > 1: res += str(cnt)
            res += last
            last = token
            cnt = 1
    if cnt > 1: res += str(cnt)
    res += last
    
    return len(res)

def solution(s):
    answer = 1001
    # 1. 1부터 s까지 자를 문자열의 길이 설정
    for length in range(1, len(s) + 1):
        tokens = list()
        for i in range(0, len(s), length):
            # 2. 설정된 길이만큼 문자열을 잘라 낸 리스트 생성 => tokens
            tokens.append(s[i:i + length])
            
        # 3. 문자열을 비교하며 리스트의 배열을 하나의 문자열로 압축
        answer = min(answer, compress(tokens))
    
    return answer