class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        miq, mxq = collections.deque(), collections.deque()
        l = res = 0
        for i, v in enumerate(nums):
            while len(mxq) > 0 and v > mxq[-1]:
                mxq.pop()
            while len(miq) > 0 and v < miq[-1]:
                miq.pop()
            mxq.append(v)
            miq.append(v)
            while len(mxq) > 0 and len(miq) > 0 and mxq[0] - miq[0] > limit:
                if nums[l] == mxq[0]: 
                    mxq.popleft()
                if nums[l] == miq[0]:
                    miq.popleft()
                l += 1
            res = max(res, i - l + 1)
        return res
    