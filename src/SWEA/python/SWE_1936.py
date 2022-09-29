# 1대1 가위바위보
## 가위 : 1, 바위 : 2, 보 : 3

a, b = map(int, input().split())
print('A' if (a - 1) == (((b - 1) + 1) % 3) else 'B')