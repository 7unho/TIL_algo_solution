# K층에 N호
t = int(input())
result = []


for _ in range(t):
    k = int(input())
    n = int(input())
    pre_floor = [int(i) for i in range(1, n + 1 )]

    if n == 1:
        result.append(1)
    else:
        for _ in range(k):
            cur_floor = []
            for i in range(1, n + 1):
                cur_floor.append(sum(pre_floor[:i]))
            pre_floor = cur_floor[:]
        result.append(cur_floor[n-1])

for i in range(t):
    print(result[i])
