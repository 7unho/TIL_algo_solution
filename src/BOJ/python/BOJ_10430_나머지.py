import sys

a, b, c = map(int, sys.stdin.readline().split())
print(f"{(a + b) % c}\n{((a%b) + (b%c)) %c}\n{(a*b)%c}\n{((a%c) * (b%c))%c}")