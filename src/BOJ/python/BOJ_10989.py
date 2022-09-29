import sys
input = sys.stdin.readline

n = int(input())

array = dict()
for _ in range(n):
    index = int(input())
    if index in array.keys():
        array[index] += 1
        continue
    array[index] = 1

index = sorted(array)

for i in index:
    for _ in range(array[i]):
        print(i)