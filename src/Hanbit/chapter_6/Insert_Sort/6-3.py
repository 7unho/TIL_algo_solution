# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
## 선택 정렬에 비해 구현 난이도는 높지만, 더 빠름

array = [7 ,5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1]  = array[j - 1], array[j]
        else:
            break

print(array)