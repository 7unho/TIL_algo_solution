# 1로 만들기
# 입력값 : N, 출력값 : 연산의 최솟값 
# 정수 X가 주어질 때, 가능한 연산은 4가지
## 1. X % 5 == 0 이면 5로 나눈다.
## 2. X % 3 == 0 이면 3으로 나눈다.
## 3. X % 2 == 0 이면 2로 나눈다.
## 4. X 에서 1을 뺀다.

import sys
input = sys.stdin.readline

d = [0] * 30001
N = int(input())

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
print(d[N])