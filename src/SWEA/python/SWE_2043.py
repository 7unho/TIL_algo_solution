# 서랍의 비밀번호
## 비밀번호 P는 000 ~ 999
## 주어지는 번호 K부터 1씩 증가하며 비밀번호 비교

p, k = map(int, input().split())
print((p - k + 1) if p >= k else 1000 - (k - p))
