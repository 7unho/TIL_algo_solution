# 뒤집기

import sys
input = sys.stdin.readline

s = input()

zero_s = s.strip().split('0')
one_s = s.strip().split('1')

zero_s = [one for one in zero_s if one != '']
one_s = [zero for zero in one_s if zero != '']


answer = max(len(zero_s), len(one_s)) - 1 if len(zero_s) != len(one_s) else len(zero_s)
print(answer)