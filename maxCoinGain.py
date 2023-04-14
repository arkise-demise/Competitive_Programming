
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-1
        total=0
        while i<j:
            total+=piles[j-1]
            i+=1
            j-=2
        return total    