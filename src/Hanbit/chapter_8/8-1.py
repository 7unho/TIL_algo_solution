# 다이나믹 프로그래밍은 동적 계획법이라고도 부른다.
## 다이나믹은 별다른 의미없이 붙여진 이름
### 다이나믹 프로그래밍 구현방법으로는 상향식 ( Bottom-Up )과 하향식 ( Top-Down )방식이 있다.

# 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있다.
## 1. 최적 부분 구조 (Optimal Substructure)
###   - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제의 답을 모아서 큰 문제를 해결

## 2. 중복되는 부분 문제 (Overlapping Subproblem)
###   - 동일한 작은 문제를 반복적으로 해결해야 한다.


# 피보나치 함수 소스코드 ( Fibonacci Function )

def fibo(x):
    if x < 1 :
        return -1
    elif x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(3))
