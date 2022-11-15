# from itertools import combinations

# D * W의 배열 K 만큼 연속되는지 체크

D, W, K = map(int, input().split())
graph = [list(map(int, input().split)) for _ in range(D)]

layer = [int(i) for i in range(D)]
A = [0] * D
B = [1] * D


def check():
    # 연속 셀 체크
    pass

def combi(start, cnt, target):
    if cnt == target:
        return check()

    for i in range(start, D):
        temp = graph[i]

        graph[i] = A
        if combi(i + 1, cnt + 1, target): return True

        graph[i] = B
        if combi(i + 1, cnt + 1, target): return True

        graph[i] = temp
    return False


def process():
    for i in range(K + 1):
        if combi(0, 0, i): return i


