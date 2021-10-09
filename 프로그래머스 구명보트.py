def solution(people, limit):
    people.sort()
    boat_num = 0
    i = 0
    j = len(people)-1
    
    while i<=j:
        boat_num += 1
        if people[i]+people[j] <= limit:
            i += 1
        
        j -= 1
    return boat_num
