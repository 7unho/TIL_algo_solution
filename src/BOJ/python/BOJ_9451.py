# 파도반 수열
## 입력값 : 테스트 케이스 (T), N 출력값: P(N)
import sys
input = sys.stdin.readline

t = int(input())

n_list = [int(input()) for _ in range(t)]

d = [0] * (101)

d[1], d[2], d[3] = 1, 1, 1
d[4], d[5] = 2, 2

for i in range(6, max(n_list) + 1):
    d[i] = d[i - 5] + d[i - 1]
    
for n in n_list:
    print(d[n])

