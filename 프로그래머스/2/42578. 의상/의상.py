def solution(clothes):
    answer = 0
    clothet = dict()
    
    for item, category in clothes:
        if category not in clothet:
            clothet[f"{category}"] = list()
        clothet[f"{category}"].append(item)
    
    answer = 1
    
    for key in clothet.keys():
        answer *= (len(clothet[key]) + 1)
    
    return answer - 1