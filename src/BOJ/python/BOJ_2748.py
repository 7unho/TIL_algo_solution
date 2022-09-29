import sys
input = sys.stdin.readline

N = int(input())

d = [0 for _ in range(N + 1)]
d[1] = 1

for i in range(2, len(d)):
    d[i] = d[i - 2] + d[i - 1]

print(d[N])