class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    if (nums[i]==nums[j]) and (i<j):
                        count+=1
        return count
        