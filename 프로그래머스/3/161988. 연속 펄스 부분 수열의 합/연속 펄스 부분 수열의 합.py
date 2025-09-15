def solution(sequence):
    # after: 짝수 index는 +, 홀수 index는 - 부호 적용
    after = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(len(sequence))]

    max_sum = after[0]
    min_sum = after[0]
    cur_max = after[0]
    cur_min = after[0]

    for i in range(1, len(after)):
        cur_max = max(after[i], cur_max + after[i])
        max_sum = max(max_sum, cur_max)

        cur_min = min(after[i], cur_min + after[i])
        min_sum = min(min_sum, cur_min)

    return max(max_sum, abs(min_sum))