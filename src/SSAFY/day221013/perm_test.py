from re import sub


test = []
N = 3
isSelected = [False] * (N + 1)
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

def combi(depth, idx):
    if depth == 2:
        print(test)
        return

    for i in range(idx, N + 1):
        test.append(i)
        combi(depth + 1, i + 1)
        test.pop()

def subset(depth):
    if depth == 3:
        if test:
            print(test)
        return
    
    test.append(depth + 1)
    subset(depth + 1)
    test.pop()
    subset(depth + 1)


perm(0)
print("=" * 28)
combi(0, 1)
print("=" * 28)
subset(0)


from itertools import permutations, combinations

li = [1, 2, 3]

print(list(permutations(li, 2)))
print(list(combinations(li, 2)))

