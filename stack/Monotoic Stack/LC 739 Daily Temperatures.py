class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        preTemp = []
        for i, t in enumerate(temperatures):
            while preTemp and preTemp[-1][1] < t:
                pI, _ = preTemp.pop()
                ans[pI] = i - pI                
            preTemp.append((i,t))
        return ans