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