import sys
coin_list = [500, 100, 50, 10, 5, 1]

n = 1000 - int(sys.stdin.readline().rstrip())
result = 0

for coin in coin_list :
    result += n // coin
    n %= coin

print(result)
