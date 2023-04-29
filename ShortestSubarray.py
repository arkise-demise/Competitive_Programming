class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pre_sums=[0]
        for i in range(n):
            pre_sums.append(nums[i]+pre_sums[-1])
        inc_q=collections.deque()
        ans=sys.maxsize
        for right,s in enumerate(pre_sums):
            while inc_q and s-pre_sums[inc_q[0]]>=k:
                ans=min(ans,right-inc_q.popleft())
            while inc_q and s<=pre_sums[inc_q[-1]]:
                inc_q.pop()
            inc_q.append(right)
        return ans if ans < sys.maxsize else -1
            