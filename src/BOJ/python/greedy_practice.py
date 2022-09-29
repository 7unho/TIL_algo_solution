# 그리디 알고리즘


## exam1. 거스름 돈
### 큰 단위가 항상 작은 단위의 배수일 때,
### 그리디 알고리즘을 통해최적의 해가 보장된다

print('=' * 24 + "exam1 code" + '=' * 24)
n = 4200
count = 0

coin_list = [500, 100, 50]

for coin in coin_list :
    count += n // coin
    n %= coin

print(count)

print('=' * 24 + "exam1 practice" + '=' * 24)

n = int(input("거스름 돈 : ").strip())
count = 0

input_coin_list = [int(i) for i in input("보유 중인 동전 종류 : ").strip().split(',')]

for coin in input_coin_list:
    count += n // coin
    n %= coin

print(f"거스름돈의 최소 개수 : {count}")

#### 화폐의 종류가 K -> 시간 복잡도는 O(K)
#### 따라서, 금액과는 무관하며 동전의 종류에만 영향을 받는다.




