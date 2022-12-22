import sys

score = int(sys.stdin.readline())
result = ''
if score // 10 >= 9:
    result = 'A'
elif score // 10 == 8:
    result = 'B'
elif score // 10 == 7:
    result = 'C'
elif score // 10 == 6:
    result = 'D'
else : result = 'F'

print(result)
