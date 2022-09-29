# 뮨서 검색

import sys
input = sys.stdin.readline

user_input = input().rstrip()
target = input().rstrip()

before = len(user_input)
user_input = user_input.replace(target, '')
after = len(user_input)

answer = 0 if after == before else (before - after) // len(target)
print(answer)
