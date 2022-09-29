# 회의실 배정
## 입력값 : N (회의의 수), (시작시간, 끝나는 시간) 출력값 : 최대 사용 가능한 회의의 수
import sys
input = sys.stdin.readline

N = int(input())
list = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간이 빠를수록, 시작시간이 빠를수록 !
list.sort(key=lambda x : (x[1], x[0]))

pre_end = 0
answer = 0

for s, e in list:
    if s >= pre_end:
        pre_end = e
        answer += 1
        continue

print(answer)