class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # print(intervals)
        intervals.sort(key=lambda i: i[0])
        # print(intervals)
        ret = []

        for start,end in intervals:
            print((start,end))
            if ret and ret[-1][1] >= start:                
                ret[-1][1] = max(end, ret[-1][1])
                # print("    ", ret)
                continue
            ret.append([start,end])
            # print(ret)
        return ret