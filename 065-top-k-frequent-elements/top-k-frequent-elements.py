class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        
        counter = Counter(nums)
        q = []
        for key, val in counter.items():
            heapq.heappush(q, (val, key))
            if len(q) > k:
                heapq.heappop(q)

        return [key for val, key in q]