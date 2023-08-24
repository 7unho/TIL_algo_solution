from itertools import combinations, permutations

def isPrime(number):
    if number < 2: return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0: return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        for c in list(combinations(numbers, i)):
            for p in list(permutations(c, i)):
                number = int(''.join(p))
                if number >= 2 and isPrime(number): answer.add(number)
                
    return len(answer)