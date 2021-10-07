def solution(name):
    count = [min(ord(i)-ord('A'),ord('Z')-ord(i)+1) for i in name]
    idx = 0
    answer = 0
    
    while True:
        answer += count[idx]
        count[idx] = 0
        if sum(count) == 0:
            return answer
        
        left, right = 1, 1
        while count[idx - left] == 0:
            left += 1
        while count[idx + right] == 0:
            right += 1
            
        if left < right: 
            answer += left
            idx += -left
        else: 
            answer += right
            idx += right
