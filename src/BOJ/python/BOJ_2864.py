# 5와 6의 차이

import sys
input = sys.stdin.readline

a, b = map(str, input().split())

answer_min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
answer_max = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(answer_min, answer_max)

