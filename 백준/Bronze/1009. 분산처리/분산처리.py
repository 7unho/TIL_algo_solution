"""
[백준 1009] 분산처리
https://www.acmicpc.net/problem/1009
"""
# 라이브러리 임포트
import sys
input = sys.stdin.readline

computers = [
    [10],
    [1],
    [6, 2, 4, 8],
    [1, 3, 9, 7],
    [6, 4],
    [5],
    [6],
    [1, 7, 9, 3],
    [6, 8, 4, 2],
    [1, 9]
]
answers = list()
for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10

    if a in [0, 1, 5, 6]:
        answers.append(computers[a][0])
        continue

    answers.append(computers[a][b % len(computers[a])])
    
for answer in answers:
    print(answer)