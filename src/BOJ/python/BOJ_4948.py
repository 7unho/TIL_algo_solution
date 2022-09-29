numRange = range(0, (123456 * 2) + 1)

def isPrime(num):
    if 0 < num <= 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prmList = [i for i in numRange if isPrime(i)]

while True:
    result = 0
    user = int(input())

    if user == 0:
        break

    for i in prmList:
        if user < i <= user * 2:
            result += 1
    print(result)