# 두 용액
## 입력 값 : 용액의 수 (N)[2 ~ 100,000] 출력값 : 0에 가장 가까운 두 수의 오름차순
import sys
input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))
array.sort()

start = 0
end = N - 1

condition = 2_000_000_001
answer = []

while True:
    # start가 end보다 커지거나 같으면 탐색이 끝난 경우이므로 탈출
    if start >= end:
        break
    # 현재 start와 end좌표의 합
    current = array[start] + array[end]

    # 현재 합이 기존 합보다 0과 가깝다면
    if condition > abs(current):
        condition = abs(current)
        answer = [array[start], array[end]]

    # 현재 합이 음수라면 -> 총합을 늘려주어야 하기 때문에 start를 증가
    if current < 0:
        start += 1
    # 현재 합이 양수라면 -> 총합을 줄어주어야 하기 떄문에 end를   감소
    else:
        end -= 1    

print(answer[0], answer[1])
