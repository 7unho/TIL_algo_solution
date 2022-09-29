import sys
input = sys.stdin.readline

def fibo(x):

    if x == 0 or x == 1 or d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 2) + fibo(x - 1)
    return d[x]

T = int(input())

array = [int(input()) for _ in range(T)]
answer = []
for i in range(2):
    d = [0] * (max(array) + 1)
    d[i], d[1 - i] = 1, 0
    fibo(max(array))
    answer.append(d)

for case in array:
    print(f"{answer[0][case]} {answer[1][case]}")