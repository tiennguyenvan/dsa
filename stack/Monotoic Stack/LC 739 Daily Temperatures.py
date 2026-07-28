class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        return ret

