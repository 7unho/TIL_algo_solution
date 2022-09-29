# 입력값 : 수열의 크기 (N)
# 출력값 : 가장 긴 증가하는 부분 수열의 길이

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.insert(0, 0)
memo = [0]

for case in cases:
