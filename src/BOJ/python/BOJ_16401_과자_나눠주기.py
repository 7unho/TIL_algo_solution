# 입력값 : 조카의 수 (M), 과자의 수 (N)
# 출력값 : 조카들에게 같은 길이로 나눠줄 수 있는 과자의 최대 길이
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

# 자를 수 있는 최소 길이 1
start = 1

# 자를 수 있는 최대 길이 
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # 입력받은 과자길이를 mid로 나눈 몫을 cnt에 저장 : mid 길이의 과자 cnt개
    for snack in snacks:
        cnt += snack // mid


    # cnt가 M보다 크다면 : 개수가 더 많다면, 길이를 늘려줘야 하므로 우측 범위 탐색
    # cnt가 M과 같다면   : 가능한 최대길이를 구하기 위해 우측 범위 탐색
    if cnt >= M:
        start = mid + 1
        answer = mid

    # cnt가 M보다 작다면 : 개수가 더 적다면, 길이를 줄여야 하므로 좌측 범위 탐색
    if cnt < M:
        end = mid - 1

print(answer)
