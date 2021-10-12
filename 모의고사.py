def solution(answers): 
    human1 = [1,2,3,4,5] * len(answers)
    human2 = [2,1,2,3,2,4,2,5] * len(answers)
    human3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    
    tup = [[1,0], [2,0], [3,0]]
    
    for i in range(len(answers)):
        if human1[i] == answers[i]: tup[0][1] += 1
        if human2[i] == answers[i]: tup[1][1] += 1
        if human3[i] == answers[i]: tup[2][1] += 1
    
    tup = sorted(tup, key=lambda x: x[1], reverse=True)
    
    if tup[0][1] == tup[1][1] == tup[2][1]: return [tup[0][0], tup[1][0], tup[2][0]]
    elif tup[0][1] == tup[1][1]: return [tup[0][0], tup[1][0]]
    else: return [tup[0][0]]
