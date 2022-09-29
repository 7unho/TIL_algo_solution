# 상향식 방식
# 1. 메모이제이션 (Memoization)
## 한 번 계산한 결과를 메모리 공간에 메모하는 기법
## - 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져온다.
## - 값을 기록해 놓는다는 점에서 캐싱(Cashing)이라고도 한다.
## - 결과 저장용 배열(리스트)를 DP 테이블이라고 부른다.

d = [0] * 100

def fibo(x):
    if x < 1:
        return -1
    elif x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(22))
print(d)