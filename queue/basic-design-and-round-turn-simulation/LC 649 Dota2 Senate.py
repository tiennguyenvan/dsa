class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = 0
        R = 0
        queue = list(senate)
        remain = Counter(queue)        
        pending = Counter()

        def winnerNameFound():
            if remain['R'] <= 0 and remain['D'] > 0: return 'Dire'
            if remain['D'] <= 0 and remain['R'] > 0: return 'Radiant'
            return ''
        def oppositeName(cur_name: str) -> str:
            return 'D' if cur_name == 'R' else 'R'
        
        while not winnerNameFound():
            qlen = len(queue)
            for i in range(qlen):
                name = queue.pop(0)
                if pending[name] > 0:
                    pending[name] -= 1
                    remain[name] -= 1
                    # print('misturn', name, remain, pending)
                    continue
                pending[oppositeName(name)] += 1
                queue.append(name)
                # print('power', name, pending, queue)
        return winnerNameFound()
                

                
        

        