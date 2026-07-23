class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedInv = sorted(intervals, key=lambda i:  i[0])

        ret = []
        for start,end in sortedInv:
            if not ret or start > ret[-1][1]:
                ret.append([start,end])
                continue
            newEnd = max(end,ret[-1][1])
            ret[-1][1] = newEnd

        return ret
