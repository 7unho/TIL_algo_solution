# 캠핑

## 입력값 : L, P, V 출력값: 이용일 수

import sys
input = sys.stdin.readline
answer_list = []

while True:
    L, P, V = map(int, input().split())
    answer = 0

    if L == 0 and P == 0 and V == 0:
        break

    answer = (V // P) * L
    answer +=  V - (V // P) * P if V - (V // P) * P <= L else L

    answer_list.append(answer)

for i in range(len(answer_list)):
    print(f"Case {i + 1}: {answer_list[i]}")