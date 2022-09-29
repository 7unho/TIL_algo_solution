# 퇴사

import sys
input = sys.stdin.readline

n = int(input())
d = [[0] for _ in range(n + 1)]

schedule = [list(map(int, input().split())) for _ in range(n)]

for i in range((n - 1), -1, -1):
    if i + schedule[i][0] > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(schedule[i][1] + d[i + schedule[i][0]], d[i + 1])

print(d[0])