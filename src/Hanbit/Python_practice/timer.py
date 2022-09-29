from random import randint
import time

arr = []
for _ in range(10000):
    arr.append(randint(1, 100))

start_time = time.time()

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

end_time = time.time()

print('선택정렬', end_time - start_time)

arr = list()
for _ in range(10000):
    arr.append(randint(1, 100))

start_time = time.time()

arr.sort()

end_time = time.time()

print('기본 정렬', end_time - start_time)