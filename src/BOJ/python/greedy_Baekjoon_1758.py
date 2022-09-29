import sys

n = int(sys.stdin.readline())
tip_list = []
sub_list = [int(i) for i in range(n)]

result = 0
for i in range(n):
    tip_list.append(int(sys.stdin.readline()))


result = sum(map(lambda a, b : a - b if a - b > 0 else 0, sorted(tip_list, reverse=True), sub_list))
print(result)
