V, P, L = map(int, input().split())
homes = list(map(int, input().split()))
polices = []
INF = int(1e9)
answer = INF
answer_list = []

def combi(depth, idx):
    global answer, answer_list
    if depth == P:
        sum = 0
        for home in homes:
            temp = INF
            for police in polices:
                temp = min(temp, min(abs(home - police), L - abs(home - police)))
            sum += temp
        
        if answer > sum:
            answer = sum
            answer_list = polices[:]
        return

    for i in range(idx, V):
        polices.append(homes[i])
        combi(depth + 1, i + 1)
        polices.pop()


combi(0, 0)
print(answer)
for item in sorted(answer_list):
    print(item, end=' ')