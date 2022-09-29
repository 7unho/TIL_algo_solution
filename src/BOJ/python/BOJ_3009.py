input_x, input_y = [], []

for _ in range(3):
    x, y = map(int, input().split())
    input_x.append(x)
    input_y.append(y)

for i in range(3):
    if input_x.count(input_x[i]) == 1:
        result_x = input_x[i]
    if input_y.count(input_y[i]) == 1:
        result_y = input_y[i]

print(result_x, result_y)