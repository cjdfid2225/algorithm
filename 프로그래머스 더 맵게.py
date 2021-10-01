import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    while heap:
        if heap[0]>=K: return answer
        
        a = heapq.heappop(heap)
        if heap!=[]:
            heapq.heappush(heap,a+(heapq.heappop(heap)*2))
            answer += 1
    return -1
