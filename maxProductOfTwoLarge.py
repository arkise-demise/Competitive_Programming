class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_array=sorted(nums)
        i=len(sorted_array)-1
        j=i-1
        return (sorted_array[i]-1) * (sorted_array[j]-1)