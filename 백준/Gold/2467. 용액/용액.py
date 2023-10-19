"""
[백준 2467] 용액
https://www.acmicpc.net/problem/2467

n := 용액의 수

answer = 합이 0과 가장 가까운 두 용액
"""
# 라이브러리 임포트
import sys
from collections import deque
input = sys.stdin.readline

MIXED = 2_000_000_001

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1
answer = [0, 0]

while True:
    case = arr[start] + arr[end]
    if start >= end: break

    if abs(case) <= MIXED:
        MIXED = abs(case)
        answer = [arr[start], arr[end]]
    
    if case <= 0:
        case -= arr[start]
        start += 1
    else:
        case -= arr[end]
        end -= 1

print(*answer)