class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums = [int(i) for i in nums]
        minhp = []
        for i in nums:
            heapq.heappush(minhp, i)
            if len(minhp) > k:
                heapq.heappop(minhp)
        return str(minhp[0])    