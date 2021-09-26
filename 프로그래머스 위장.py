from collections import defaultdict
def solution(clothes):
    hash_map = defaultdict(int)
    for field in clothes:
        hash_map[field[1]] += 1
        
    answer = 1
    for i in hash_map:
        if len(hash_map) == 1:
            return hash_map[i]
        else:
            answer *= (hash_map[i]+1)
            
    return answer-1
