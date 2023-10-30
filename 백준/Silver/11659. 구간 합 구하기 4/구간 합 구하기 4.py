import sys
input = sys.stdin.readline

# 입력값 : N(수의 개수), M(연산 횟수)
# 출력값 : (시작, 끝)범위의 구간합

N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
sum = numbers[:]
for i in range(2, (N + 1)):
    sum[i] += sum[i - 1]
    
for _ in range(M):
    s, e = map(int, input().split())

    print(sum[e] - sum[s - 1])