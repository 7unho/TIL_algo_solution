# 입력값 : 조카의 수 (M), 과자의 수 (N)
# 출력값 : 조카들에게 같은 길이로 나눠줄 수 있는 과자의 최대 길이
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start = 1
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for snack in snacks:
        cnt += snack // mid

    if cnt >= M:
        start = mid + 1
        answer = mid

    if cnt < M:
        end = mid - 1
        continue

print(answer)
