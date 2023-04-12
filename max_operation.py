class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left=0;right=len(nums)-1;count=0
        while left<right:
            mid=nums[left]+nums[right]
            if mid==k:
                count+=1
                right-=1
                left+=1
            elif mid>k:
                right-=1
            else:
                left+=1
        return count              