"""
소프티어 LV3. 조립라인
https://softeer.ai/practice/6287

1 <= A, B <= N

N := 작업장의 개수

a작업시간, b작업시간, 이동시간, 이동시간
an작업 시간, bn작업 시간
"""
# == Import 선언 부
import sys
input = sys.stdin.readline

# == 변수 선언 부
A = 0
B = 1

N = int(input())
jobTime = list()
moveTime = list()

for _ in range(N - 1):
  aJob, bJob, atob, btoa = map(int, input().split())
  jobTime.append([aJob, bJob])
  moveTime.append([atob, btoa])
  
jobTime.append(list(map(int, input().split())))

answer = [
  [jobTime[i][A] for i in range(N)],
  [jobTime[i][B] for i in range(N)],
]

# == process
for i in range(1, N):
  at, bt = jobTime[i]
  atob, btoa = moveTime[i - 1]
  
  answer[A][i] = min(answer[A][i - 1] + at, answer[B][i - 1] + btoa + at)
  answer[B][i] = min(answer[B][i - 1] + bt, answer[A][i - 1] + atob + bt)

print(min(answer[A][N - 1], answer[B][N - 1]))
