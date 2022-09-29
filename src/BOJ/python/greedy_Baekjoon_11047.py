# 백준 알고리즘 11047_greedy 알고리즘
## 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

input_data = [int(i) for i in input().split(' ')]
input_N, input_K = input_data[0], input_data[1]

coin_list = list()
count = 0


for i in range(1, input_N + 1) :
    coin_list.append(int(input()))

for coin in sorted(coin_list, reverse=True):
    count += input_K // coin
    input_K %= coin

print(count)