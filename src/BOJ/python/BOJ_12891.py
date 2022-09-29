from socketserver import ForkingMixIn


S, T = map(int, input().split())
input = input()


A_cnt, C_cnt, G_cnt, T_cnt = map(int, input().split())

for i in range(S - T + 1):
    temp = input[i : i + T]

    for ch in temp:
        print(ch)