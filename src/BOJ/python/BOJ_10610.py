# 30
## n의 각 자릿수들을 섞어서 30의 배수가 되는 가장 큰 수 출력

import sys
input = sys.stdin.readline

n = list(input().rstrip())
n.sort(reverse=True)
total = [int(i) for i in n]
total = sum(total)

answer = -1 if total % 3 != 0 or '0' not in n else ''.join(n)
print(answer)