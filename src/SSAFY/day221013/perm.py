N = 3
isSelected = [False] * (N + 1)
test = list()

def perm(depth):
    if depth == 2:
        print(test)
        return
    
    for i in range(1, N + 1):
        if isSelected[i]: continue

        isSelected[i] = True
        test.append(i)
        perm(depth + 1)
        isSelected[i] = False
        test.pop()

def subset(depth):
    if depth == 2:
        if test: print(test)
        return

    test.append(depth + 1)
    subset(depth + 1)
    test.pop()
    subset(depth + 1)

def combi(depth, idx):
    if depth == 2:
        print(test)
        return

    for i in range(idx, N + 1):
        test.append(i)
        combi(depth + 1, i + 1)
        test.pop()


perm(0)
subset(0)
combi(0, 1)