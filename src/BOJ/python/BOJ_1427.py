import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))

for item in sorted(n, reverse=True):
    print(item,end='')