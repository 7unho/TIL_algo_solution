# 신규 아이디 추천

def solution(new_id):

    # 1단계
    new_id = new_id.lower()
    print(f"1단계 : {new_id}")

    # 2단계
    new_id = list(new_id.rstrip())
    
    for i in range(len(new_id)):
        if not new_id[i].isalnum() and new_id[i] not in ['-', '_', '.'] :
            new_id[i] = ''

        
    new_id = ''.join(new_id)
    print(f"2단계 : {new_id}")
    
    # 3단계
    new_id = new_id.replace('...', '.').replace('..', '.')
    print(f"3단계 : {new_id}")

    # 4단계
    new_id = list(new_id.rstrip()) if new_id is not '' else ['']
    if new_id[0] == '.':
        new_id.remove(new_id[0])
    elif new_id[len(new_id) - 1] == '.':
        new_id.remove(new_id[len(new_id) - 1])
    
    print(f"4단계 : {''.join(new_id)}")
    
    # 5단계
    print(new_id == [''])
    if new_id == []:
        new_id = ['a']
    
    print(f"5단계 : {''.join(new_id)}")

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[len(new_id) - 1] == '.':
            new_id.remove(new_id[len(new_id) - 1])
        
        print(f"6단계 : {''.join(new_id)}")

    # 7단계
    elif len(new_id) <= 2:
        temp = new_id[len(new_id) - 1]
        while len(new_id) < 3:
            new_id.append(temp)
    
    answer = ''.join(new_id)
    return answer


test_case = ["...!@BaT#*..y.abcdefghijklm", 
             "z-+.^.",
             "=.=",
             "123_.def",
             "abcdefghijklmn.p",
             "",
             "..!&ㄹㄹㄹscfgss$!@.."]

for case in test_case:
    print(solution(case))