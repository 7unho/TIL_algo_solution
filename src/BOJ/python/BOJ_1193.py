input_n = int(input())

boundary = 1
i = 1

while input_n > boundary:
    i += 1
    boundary = boundary +  i * 1

point = boundary - input_n
print(f"{i - point}/{1 + point}" if i % 2 == 0 else f"{1 + point}/{i - point}")
