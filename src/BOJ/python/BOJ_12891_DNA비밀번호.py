import sys
input = sys.stdin.readline
# 입력값 : 문자열 길이(l), 부분 문자열의 길이(k)
#         A, C, G, T의 최소개수

def isValid():
    global ACGT, cnt

    for i in range(4):
        if cnt[i] > ACGT[f"{dna[i]}"]: return False

    return True

l, k = map(int, input().split())
pw = list(input().rstrip())
cnt = list(map(int, input().split()))

dna = ['A', 'C', 'G', 'T']
window = 0
answer = 0
start = 0
ACGT = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}

# 1. 슬라이딩 윈도우로 부분 문자열 탐색
## for문으로 origin 탐색
## window가 k보다 크다면, window 감소 시키고 문자열 첫글자 삭제
for end in range(l):
    window += 1
    ACGT[f"{pw[end]}"] += 1
    ## window가 k보다 작다면, window 증가 시키고 문자열에 추가
    if window > k:
        ACGT[f"{pw[start]}"] -= 1
        window -= 1
        start += 1
    
    if window == k and isValid(): answer += 1
    

print(answer)
