import math

r = int(input())

result_circle = r**2*math.pi
result_square = 2 * (r ** 2)
print(f"{format(result_circle, '.6f')}\n{format(result_square, '.6f')}")