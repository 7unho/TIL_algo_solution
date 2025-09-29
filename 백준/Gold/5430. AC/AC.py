"""
R : 배열 뒤집기
D : 첫번째 버리기, 배열 비어있을 땐 에러
"""
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    commands = list(input())
    n = int(input())
    isError = False
    reverse_count = 0

    if n == 0:
        input()
        arr = deque()
    else: 
        arr = deque(list(map(int, input().rstrip()[1:-1].split(","))))

    for command in commands:
        if command == 'D' and not arr:
            isError = True
            break

        if command == 'R':
            reverse_count += 1
            continue
        
        if command == 'D':
            if reverse_count % 2 == 1:
                arr.pop()
            else:
                arr.popleft()
                
    if reverse_count % 2 == 1:
        arr.reverse()
        
    message = "error" if isError else f"[{','.join(map(str, arr))}]"
    print(message)
