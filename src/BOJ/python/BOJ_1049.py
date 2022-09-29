# 기타줄
## 입력값 : N개의 기타줄, M개의 브랜드
##        6개 가격, 낱개 가격

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
pieces_list = []
piece_list = []
for _ in range(m):
    pieces, piece = map(int, input().split())
    pieces_list.append(pieces)
    piece_list.append(piece)

pieces_list.sort()
piece_list.sort()

answer = min(
             (n // 6) * pieces_list[0] + (n % 6) * piece_list[0]
             , n * piece_list[0]
             , ((n // 6) + 1 ) * pieces_list[0]
             )
print(answer)