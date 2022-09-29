# 숫자가 같은 배수
## 입력 받은 n의 자릿수를 재배열하여 N의 배수가 가능한지

import sys
input = sys.stdin.readline

t = int(input())
answers = []
for i in range(t):
        n = int(input())
        n_list = []
        i = 2
        while True:
            if len(str(n * i)) > len(str(n)):
                break

            n_list.append(list(map(int, str(n * i))))
            i += 1

        n_list = [sorted(item) for item in n_list]
        n = list(map(int, str(n).rstrip()))
        n.sort()
        answer = 'possible' if n in n_list else 'impossible'
        answers.append(answer)
    
for i in range(len(answers)):
    print(f"#{i + 1} {answers[i]}")

