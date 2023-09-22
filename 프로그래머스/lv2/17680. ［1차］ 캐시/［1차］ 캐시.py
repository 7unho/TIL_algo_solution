# 실행시간 1 if hit else 5

def process(city, cache, cacheSize):
    # 시티가 캐시에 있다면, cache hit
    if city in cache:
        cache.remove(city)
        cache.insert(0, city)
        return 1
    
    if len(cache) >= cacheSize: cache.pop()
    cache.insert(0, city)
    
    return 5
    

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0: return len(cities) * 5
    for city in cities:
        answer += process(city.upper(), cache, cacheSize)
    return answer