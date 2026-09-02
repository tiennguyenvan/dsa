class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        getTrust = [0] * n
        giveTrust = [0] * n

        for a,b in trust:
            getTrust[b-1]+=1
            giveTrust[a-1]+=1

        for i in range(n):
            if getTrust[i] == n-1 and giveTrust[i] == 0:
                return i+1
        return -1
