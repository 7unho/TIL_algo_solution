import sys
input = sys.stdin.readline

array = [int(input()) for _ in range(9)]
array.sort()

target = sum(array) - 100

for i in range(9):
    if len(array) < 9:
        break
    if array[i] + array[8] < target:
        continue
    for j in range((i + 1), 9):
        if array[i] + array[j] == target:
            num1, num2 = array[i], array[j]
            
            array.remove(num1)
            array.remove(num2)

            array.sort()

            for answer in array:
                print(answer)
            
            break