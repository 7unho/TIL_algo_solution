# 달팽이 게임
# A미터 올라가고, B미터 떨어지는 달팽이가 높이가 V인 정상까지 며칠이 소요되는지
import math

a, b, v = map(int, input().split(' '))
result = math.ceil(( (v - a) / ( a - b))) + 1
print(result)
