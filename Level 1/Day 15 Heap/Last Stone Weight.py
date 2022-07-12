import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        # while len(stones)>1:
        #     x = stones[-1]
        #     y = stones[-2]
        #     stones = stones[:-2]
        #     if x!=y:
        #         stones.append(x-y)
        #         stones.sort()
        # return stones[0] if len(stones)==1 else 0
        for i in range(len(stones)):
            stones[i] = - stones[i]
        heapq.heapify(stones)
        while(len(stones) > 1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones, x-y)
        return 0 if len(stones) == 0 else -stones[0]
        