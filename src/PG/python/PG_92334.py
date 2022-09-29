# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_dict = dict()
    report_count = dict()
    target_list = []

    for user in id_list:
        report_dict[user] = []
        report_count[user] = 0

    for i in range(len(report)):
        reporter, reported = map(str, report[i].split(' '))
        if reported not in report_dict[reporter]:
            report_dict[reporter].append(reported)
            report_count[reported] += 1
        
    print(report_dict)
    print(report_count)

    for user, count in report_count.items():
        if count >= k:
            target_list.append(user)
    
    for target in target_list:
        idx = 0

        for case in report_dict.values():
            if target in case:
                answer[idx] += 1
            
            idx += 1

    return answer

id_list = ['muzi', 'apeach', 'frodo', 'neo']
report = ['muzi frodo','muzi frodo' , 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi']



print(solution(id_list, report, 2))

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer