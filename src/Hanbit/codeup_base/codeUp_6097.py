h, w = map(int, input().split())

resList = [[0 for col in range(w)] for row in range(h)]

n = int(input())

for i in range(n):
    l, d, y, x = map(int, input().split())

    if d == 0:
        for j in range(l):
            resList[y-1][(x-1) + j] = 1

    if d == 1:
        for k in range(l):
            resList[(y-1) + k][x-1] = 1

for res in resList:
    for item in res:
        print(item, end=' ')
    print()

