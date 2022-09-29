t = int(input())

def isPrime(num):
    if 0 < num <= 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prmList = list()

for i in range(1, 10001):
    if not isPrime(i):
        continue
    prmList.append(i)


for j in range(t):
    n = int(input())

    for k in range(int(n/2), 1, -1):
        if k not in prmList:
            continue

        if (n - k) in prmList:
            print(f"{k} {n-k}")
            break
    # print(f"{result[int(len(result) / 2)][0]} {result[int(len(result) / 2)][1]}" if len(result) % 2 != 0
    #       else f"{result[int(len(result) / 2) - 1][0]} {result[int(len(result) / 2) - 1][1]}")
