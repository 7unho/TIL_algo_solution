# 입력값 : N(사람의 수), M(파티의 수)
# 출력깂 : 최대 거짓말의 수
# 조건 1. 진실을 아는 사람이 있다면, 진실을 말해야 한다.
# 조건 2. 모순이 발생하면 안 된다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knowledge = set(list(map(int, input().split()))[1:])
parties = []
answer = 0

parties = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

for _ in range(M):
    for i in range(M):
        party = parties[i]

        # 현재 파티에 아는 사람이 존재한다면,
        if not party & knowledge: continue
            # 해당 파티원들을 아는 사람에 추가
        knowledge |= party

for party in parties:
    if party & knowledge: continue
    answer +=1


print(answer)
