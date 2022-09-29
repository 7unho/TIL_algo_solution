import sys
input = sys.stdin.readline

N = int(input())

memberList = []

for i in range(1, N + 1):
    age, name = map(str, input().split())
    rank = i
    memberList.append([int(age), name, rank])

memberList.sort(key=lambda x : (x[0], x[2]))

for member in memberList:
    print(f"{member[0]} {member[1]}")