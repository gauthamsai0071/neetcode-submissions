class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        n=len(stones)
        
        for i in range(n):
            heapq.heappush(maxheap, -stones[i])
        
        while len(maxheap)>1:
            first=-heapq.heappop(maxheap)
            second=-heapq.heappop(maxheap)
            if first!=second:
                heapq.heappush(maxheap, -(first-second))
        
        return -maxheap[0] if len(maxheap)>0 else 0