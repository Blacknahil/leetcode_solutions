class Solution:
    def nthUglyNumber(self, n: int) -> int:
        prev=1
        heap=[1]
        for _ in range(n):
            cur=heapq.heappop(heap)
            while heap and cur==prev:
                cur=heapq.heappop(heap)
            heapq.heappush(heap,2*cur)
            heapq.heappush(heap,3*cur)
            heapq.heappush(heap,5*cur)
            prev=cur
            # print(\prev\,prev)
        
        return prev


            


