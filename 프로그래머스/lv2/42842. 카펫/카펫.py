# 노란색 기준으로. 높이를 늘려가면서 찾기.

# brown, yellow = 10, 2 # [4, 3]
# brown, yellow = 8, 1 # [3, 3]
# brown, yellow = 24, 24 # [8, 6]


def getDivisor(sum):
    divisor = set()

    for i in range(3, int(sum ** 0.5) + 1):
        if sum % i != 0: continue

        divisor.add((sum // i, i))

    return divisor

def solution(brown, yellow):
    divisor = getDivisor(brown + yellow)

    for width, height in divisor:
        # 가능한 약수의 조합에서
        ## 옐로우가 될 수 있는 값들을 보내준다.
        w_list = [i for i in range(2 - (width % 2), width, 2)]
        h_list = [i for i in range(2 - (height % 2), height, 2)]

        for w in w_list:
            for h in h_list:
                if w * h != yellow: continue

                return [width, height]
