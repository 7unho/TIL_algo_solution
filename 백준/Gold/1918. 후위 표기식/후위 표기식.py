# # 입력값 : 중위 표기식
# # 출력값 : 후위 표기식
import sys
input = sys.stdin.readline

inorder = list(input().rstrip() + ')')
stack = ['(']
answer = []


def braketClear(item):
    global stack, answer
    while True:
        top = stack[-1]
    
        if item == ')':
            if top == '(':
                stack.pop()
                return
            
            answer.append(stack.pop())
        
        if item != ')':
            if top == '(' or item in ('*', '/') and top in ('+', '-'):
                stack.append(item)
                return
            
            answer.append(stack.pop())

    # if item == ')':
    #     while True:
    #         top = stack[-1]
            
    #         if top == '(':
    #             stack.pop()
    #             return

    #         answer.append(stack.pop())
    
    # while True:
    #     top = stack[-1]

    #     if top == '(' or item in ('*', '/') and top in ('+', '-'):
    #         stack.append(item)
    #         return
        
    #     answer.append(stack.pop())

for item in inorder:
    if item.isalpha():
        answer.append(item)
        continue

    top = stack[-1]
    # ')'를 받을 때마다, 스택을 정리.
    if item == ')' or item in ('+', '-') or (item in ('*', '/') and top in ('*', '/')): 
        braketClear(item)
        continue

    stack.append(item)
    

print(''.join(answer))

