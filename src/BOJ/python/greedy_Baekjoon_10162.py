import sys

t = int(sys.stdin.readline().rstrip())

btn_list = [300, 60, 10]
result_list = [0, 0, 0]

for i in range(len(btn_list)):
    result_list[i] += t // btn_list[i]
    t %= btn_list[i]

if t == 0:
    print(result_list[0], result_list[1], result_list[2])
else:
    print('-1')