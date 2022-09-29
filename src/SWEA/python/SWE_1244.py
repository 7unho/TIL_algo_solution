# 최대 상금 구하기

from copy import deepcopy

def solution(arrays, cnt):
    result = []

    if cnt == int(k):
        return arrays

    for array in arrays:
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                cp_array = deepcopy(array)
                cp_array[i], cp_array[j] = cp_array[j], cp_array[i]
                
                if cp_array not in result:
                    result.append(cp_array)
                
    return solution(result, cnt + 1)
        

for i in range(int(input())):
    array, k = map(str, input().split())
    array = list(array)

    res = solution([array], 0)
    answer = ''.join(max(res))
    print(f"#{i + 1} {answer}")