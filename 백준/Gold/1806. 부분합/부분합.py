"""
[백준 1806] 부분합
https://www.acmicpc.net/problem/1806

N := 수열의 길이
S := 만들어야할 수

answer = N의 부분 수열 중, 합이 S인 가장 짧은 수열의 길이
"""
# 라이브러리 임포트
import sys
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
_sum = arr[0]
answer = n + 1
while True:        
    # 합이 S 보다 작다면, end 증가
    if _sum < s: 
        if end == n - 1: break
        end += 1
        _sum += arr[end]
    elif _sum >= s:
        answer = min(answer, end - start + 1)
        _sum -= arr[start]
        start += 1

print(0 if answer == n + 1 else answer)