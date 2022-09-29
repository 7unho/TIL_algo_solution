# 계수 정렬
## 데이터의 크기 버위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len((array))):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')