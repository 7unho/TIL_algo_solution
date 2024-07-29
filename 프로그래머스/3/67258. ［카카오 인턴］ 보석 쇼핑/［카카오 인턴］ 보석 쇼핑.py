from collections import defaultdict
def solution(gems):
    N, M = len(gems), len(set(gems))
    end = 0
    gemCounter = defaultdict(int)
    _range = int(100_001)
    answer = [-1, -1]
    for start in range(N):
        # 1. M보다 작고, end가 범위 안일 경우
        while len(gemCounter) < M and end < N:
            gemCounter[gems[end]] += 1
            end += 1
        # 2. M인 경우, e - s값이 최소일 때만, answer 변경
        if len(gemCounter) == M:
            if end - start - 1 < _range:
                _range = end - start - 1
                answer = [start + 1, end]
        # 3. gemCnt에서 start 제거 -> 다음 루프에 start가 증가하므로
        if gemCounter[gems[start]] == 1:
            del gemCounter[gems[start]]
        else:
            gemCounter[gems[start]] -= 1

    return answer