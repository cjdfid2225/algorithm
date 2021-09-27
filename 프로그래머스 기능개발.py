def solution(progresses, speeds):
    answer = []
    middle = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            middle.append((100-progresses[i])//speeds[i])
        else:
            middle.append(((100-progresses[i])//speeds[i])+1)
    
    queue = []
    while middle:
        num = 1
        current = middle.pop(0)
        for _ in range(len(middle)):
            if current >= middle[0]:
                middle.pop(0)
                num += 1
            else:
                break
        queue.append(num)
    return queue
