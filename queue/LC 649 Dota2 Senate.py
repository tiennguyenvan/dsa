class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = deque()
        R = deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'D':
                D.append(i)
                continue
            R.append(i)

        while D and R:
            D0 = D.popleft()
            R0 = R.popleft()
            banningDire = R0 < D0
            if banningDire:
                R.append(R0 + n)
                continue
            D.append(D0 + n)
            
        
        return 'Dire' if D else 'Radiant'
