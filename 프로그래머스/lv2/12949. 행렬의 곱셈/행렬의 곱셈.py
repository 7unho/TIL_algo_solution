def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr2[0])

    answer = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer