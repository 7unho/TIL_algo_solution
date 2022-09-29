n = input()
result = 0

for h in range(int(n) + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result = result + 1

print(result)