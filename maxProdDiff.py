class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortedNum=[]
        sortedNum=sorted(nums)
        prod1=sortedNum[0]*sortedNum[1]
        prod2=sortedNum[-1]*sortedNum[-2]
        return prod2-prod1