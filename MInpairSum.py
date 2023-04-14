class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        max_pair=0
        while i<j:
            max_pair=max(max_pair,nums[i]+nums[j])
            i+=1
            j-=1
        return max_pair