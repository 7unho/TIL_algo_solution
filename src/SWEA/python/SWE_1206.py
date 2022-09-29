# View
answers = []

for i in range(10):
    n = int(input())
    array = list(map(int, input().split()))
    answer = 0
    for i in range(2, n - 2):
        before_cur = [array[i - 2], array[i - 1]]
        after_cur = [array[i + 2], array[i + 1]]
        if max(before_cur + after_cur) < array[i]:
            answer += array[i] - max(before_cur + after_cur)
    
    answers.append(answer)

for i in range(10):
    print(f"#{i + 1} {answers[i]}")