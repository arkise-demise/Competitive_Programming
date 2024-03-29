class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={}
        for task in tasks:
            if task not in freq:
                freq [task]=1
            else:
                freq[task]+=1
        freq=[value for key,value in freq.items()]
        max_freq=max(freq)
        max_freq_tasks=freq.count(max_freq)
        return max(len(tasks),(max_freq-1)*(n+1)+max_freq_tasks)