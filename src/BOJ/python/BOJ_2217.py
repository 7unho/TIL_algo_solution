import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

answer = [array[i] * (i+1) for i in range(len(array))]
print(max(answer))