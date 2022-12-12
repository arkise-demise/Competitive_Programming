class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNumbers =sorted(nums)
        dict ={}
        result =[]
        for i in range(len(sortedNumbers)):
            if sortedNumbers[i] not in dict:
                dict[sortedNumbers[i]]= i
        for i in nums:
            result.append(dict[i])  
        return result          
            