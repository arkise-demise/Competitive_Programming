class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        if not temperatures: return []
        res = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                stack_top_index = stack.pop()[1]
                count = index - stack_top_index
                res[stack_top_index]=count
            stack.append((val, index))
        return res