def solution(numbers):
    answer = ''
    str_num = []
    for i in range(len(numbers)):
        str_num.append([i,str(numbers[i])*3])
    str_num.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(numbers)):
        answer += str(numbers[str_num[i][0]])
    if [0]*len(numbers)==numbers:
        return '0'
    return answer
