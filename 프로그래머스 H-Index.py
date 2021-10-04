def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    
    return answer
