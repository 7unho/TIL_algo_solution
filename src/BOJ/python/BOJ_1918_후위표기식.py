# # 입력값 : 중위 표기식
# # 출력값 : 후위 표기식
import sys
input = sys.stdin.readline

inorder = list(input().rstrip() + ')')
stack = ['(']
answer = []


def solution(item):
    global stack, answer
    while True:
        top = stack[-1]

        if top == '(':
            if item == ')': stack.pop()
            else: stack.append(item)

            return
        
        if item in ('*', '/') and top in ('+', '-'):
            stack.append(item)
            return
        
        answer.append(stack.pop())

for item in inorder:
    if item.isalpha():
        answer.append(item)
        continue

    top = stack[-1]
    # ')'를 받을 때마다, 스택을 정리.
    if item == ')' or item in ('+', '-') or (item in ('*', '/') and top in ('*', '/')): 
        solution(item)
        continue

    stack.append(item)

print(''.join(answer))

