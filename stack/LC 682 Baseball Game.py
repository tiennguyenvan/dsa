class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        records = []
        for o in operations:            
            if o == '+':
                a = records[-1]
                b = records[-2]
                score = a + b
                records.append(score)
                x += score
                continue
            
            if o == 'D':
                score = records[-1] * 2
                records.append(score)
                x += score
                continue

            if o == 'C':
                score = records.pop()
                x -= score
                continue

            score = int(o)
            x += score
            records.append(score)
                
        return x