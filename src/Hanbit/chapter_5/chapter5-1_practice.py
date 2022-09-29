# stack 구조의 리스트

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()

stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])
print(stack)


# queue 구조의 리스트
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

queueToList = list(queue)
print(queueToList)

# 재귀함수 : 자기 자신을 다시 호출하는 함수

def recursive_function():
    print("재귀 함수를 호출합니다")
    recursive_function()

#recursive_function()

# 재귀함수의 종료조건

def recursive_function(i):
    # 10번 째 출력시 종료
    if i == 10:
        return
    print(f"{i}번째 재귀함수에서{i+1}번째 재귀함수를 호출합니다")
    recursive_function(i+1)
    print(f"{i}번째 재귀함수를 종료합니다")

#recursive_function(1)


# 2가지 방식으로 구현한 팩토리얼 예제

## 2-1. 반복적으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

## 2-2. 재귀 함수로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(5))
print(factorial_recursive(5))
