# 신입사원
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    array.sort(key=lambda x : x[0])
    count = 1
    target = array[0][1]

    for i in range(1, n):
        if target > array[i][1]:
            count += 1
            target = array[i][1]

    print(count)
    