# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]


def solution(survey, choices):
    answer = ''
    test = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    for i in range(len(survey)):
        if choices[i] <= 3:
            test[survey[i][0]] += 4 - choices[i]
        elif choices[i] >= 5:
            test[survey[i][1]] += choices[i] - 4

    if test['R'] >= test['T']:
        answer += 'R'
    else:
        answer += 'T'
    if test['C'] >= test['F']:
        answer += 'C'
    else:
        answer += 'F'
    if test['J'] >= test['M']:
        answer += 'J'
    else:
        answer += 'M'
    if test['A'] >= test['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer


print(solution(survey, choices))
