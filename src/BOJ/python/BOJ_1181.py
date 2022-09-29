import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(input().rstrip())

array = list(set(sorted(array)))
array.sort()
array.sort(key=len)

for item in array:
    print(item)
