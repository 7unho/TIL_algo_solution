# 가장 긴 바이토닉 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dpu = [1 for _ in range(n)]
dpd = [1 for _ in range(n)]
answer = []
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dpu[i] = max(dpu[i], dpu[j] + 1)

        if array[j] > array[i]:
            dpd[i] = max(dpd[i], dpd[j] + 1)
    answer.append(dpu[i] + dpd[i] - 1)

print(dpu)
print(dpd)
print(answer)