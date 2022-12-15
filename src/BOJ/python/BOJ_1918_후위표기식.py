# # 입력값 : 중위 표기식
# # 출력값 : 후위 표기식
import sys
input = sys.stdin.readline

inorder = list('(' + input().rstrip() + ')')
stack = []
answer = []

print(inorder)

