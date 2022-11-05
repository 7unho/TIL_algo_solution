import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))

for _ in range(K):
    start, end = map(int, input().split())
    start = start - 1
    print(f"{sum(scores[start:end]) / (end - start):.2f}")