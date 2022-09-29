# 피보나치 시간복잡도 확인 ( 상향식 )

from re import L


d = [0] * 100

def fibo(x):
    print(f"f({str(x)})", end=" ")
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)

# 다이나