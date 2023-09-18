import sys
input = sys.stdin.readline

N = int(input())
items = list(map(int, input().split()))
sortItems = list(set(items))
sortItems.sort()

answer = {}
for i, item in enumerate(sortItems):
    answer[item] = i

for item in items:
    print(answer[item])