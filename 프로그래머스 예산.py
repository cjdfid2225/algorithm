def solution(d, budget):
    d = sorted(d)
    sum, count = 0, 0
    for i in d:
        if sum + i <= budget:
            sum += i;count += 1
    return count
