class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        counter = 0
        n = len(num)
    
        if n == k: return "0"
    
        for i in range(n):
            while k and res and res[-1] > num[i]:
                res.pop()
                k -= 1
            res.append(num[i])

    
        while k:
            res.pop()
            k -= 1
        
        return "".join(res).lstrip('0') or "0"
            