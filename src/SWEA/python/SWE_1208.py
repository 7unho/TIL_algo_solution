# 덤프

for i in range(1):
    cnt = int(input())
    array = list(map(int, input().split()))
    answer = 0

    while True:
        if cnt == 0:
            answer = max(array) - min(array)
            break

        array[array.index(max(array))] -= 1
        array[array.index((min(array)))] += 1
        cnt -= 1
    
    print(f"#{i + 1} {answer}")