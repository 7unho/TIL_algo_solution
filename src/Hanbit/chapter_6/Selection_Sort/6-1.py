#선택 정렬
## 처리되지 않은 데이터중에서 가장 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 변경

array = [7 ,5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]
