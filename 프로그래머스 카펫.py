def solution(brown, yellow):
    for i in range(1,brown):
        for j in range(1,brown):
            if i*j == (brown+yellow) and (i+j)*2-4 == brown: 
                answer = [i,j]
    return answer
