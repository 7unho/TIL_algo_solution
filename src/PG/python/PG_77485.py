# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    graph = [[int(j + columns * i) for j in range(1, columns + 1)] for i in range(rows)]
    answers = list()

    for start_x, start_y, end_x, end_y in queries:
        graph, answer = rotate(graph, start_x, start_y, end_x, end_y)
        answers.append(answer)

    return answers
        

def rotate(graph, start_x, start_y, end_x, end_y):
    data = [graph[start_x - 1][start_y - 1]]

    # 왼쪽 값
    for y in range(start_y, end_y):
        data.append(graph[start_x - 1][y])
        graph[start_x - 1][y] = data[-2]
    # 위쪽 값
    for x in range(start_x, end_x):
        data.append(graph[x][end_y - 1])
        graph[x][end_y - 1] = data[-2]
    # 오른쪽 값
    for y in range(end_y - 2, start_y - 2, -1):
        data.append(graph[end_x - 1][y])
        graph[end_x - 1][y] = data[-2]
    # 아래쪽 값
    for x in range(end_x - 2 , start_x - 2, -1):
        data.append(graph[x][start_y - 1])
        graph[x][start_y - 1] = data[-2]
    
    return graph, min(data)
