class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count,size,i = 0, 0, 0
        hashtable = collections.Counter(arr).most_common()
        while size < len(arr)//2:
            size += hashtable[i][1]
            i += 1
            count+=1
        return count