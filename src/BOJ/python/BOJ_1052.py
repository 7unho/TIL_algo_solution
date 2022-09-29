# 물병
## 입력값 : 물병의 개수( N ), 한 번에 K개의 물병을 옮길 때 출력값 : K개를 넘지 않는 비어있지 않은 물병
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0

# 물병의 개수를 2진수로 변환 후 1의 개수 카운팅
# 2진수 N의 1의 개수가 K를 넘지 않을 때 까지 물병(answer)을 구입한다.
while bin(N).count('1') > K:
    N += 1
    answer += 1

print(answer)