class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        res = []
        for i in range(n):
            cur_max = max(arr[0:n-i])
            j = 0
            while arr[j] != cur_max:
                j += 1
            arr[:j+1] = reversed(arr[:j+1])
            res.append(j+1)
            arr[:n-i] = reversed(arr[:n-i])
            res.append(n-i)
        return res