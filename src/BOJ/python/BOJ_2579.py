# 계단 오르기
## 입력값 : 계단의 개수, 출력값 : 점수의 최댓값
### 한 번에 1, 2칸씩 이동 가능하며, 연속된 세 개의 계단을 밟으면 안되고, 마지막 계단은 꼭 밟아야 한다.
import sys
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
array.insert(0, 0)
d = [0] * (N + 1)
d[1] = array[1]

for i in range(2, (N + 1)):
    d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3])

print(d[N])