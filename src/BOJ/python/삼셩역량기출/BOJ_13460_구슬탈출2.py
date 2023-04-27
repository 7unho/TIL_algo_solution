N, M = map(int, input().split())

isSelected = [False] * (N + 1)
test = []
cnt = 0
def perm(depth):
    if depth == M:
        print(test)
        return
    
    for i in range(1, N + 1):
        if isSelected[i]: continue

        isSelected[i] = True
        test.append(i)
        perm(depth + 1)
        test.pop()
        isSelected[i] = False

def combi(depth, idx):
    if depth == M:
        print(test)
        return
    
    for i in range(idx, N + 1):
        if isSelected[i]: continue
        isSelected[i] = True
        test.append(i)
        combi(depth + 1, i + 1)
        test.pop()
        isSelected[i] = False

def subset(depth):
    global cnt
    if depth == N:
        if test:
            cnt += 1
            print(test)
        return
    
    test.append(depth + 1)
    subset(depth + 1)
    test.pop()
    subset(depth + 1)

# perm(0)
# subset(0)
subset(0)
print(cnt)