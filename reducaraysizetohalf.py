class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        h={}
        for num in arr:
            if num not in h:
                h[num]=1
            else:
                h[num]+=1
        sorted_values=sorted(h.values(),reverse=True)
        ans=0
        a=len(arr)
        b=len(arr)//2
        for i in sorted_values:
            a-=i
            if a>b:
                ans+=1
            else:
                ans+=1
                break
        return ans