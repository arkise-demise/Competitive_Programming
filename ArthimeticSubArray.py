class Solution:
 
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def chek(nums):
            if len(nums)<2:
                return False
            if len(nums)==2:
                return True
            diff=nums[1]-nums[0]
            for i in range(1,len(nums)-1):
                if nums[i+1]-nums[i]!=diff:
                    return False
            return True
        result=[]
        for i in range(len(l)):
            sub_array=nums[l[i]:r[i]+1]
            sub_array.sort() 
            if chek(sub_array):
                result.append(True)
            else:
                result.append(False)
        return result                               