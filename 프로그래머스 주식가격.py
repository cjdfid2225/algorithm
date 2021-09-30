def solution(prices):
    answers = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answers[i] += 1
    return answers
