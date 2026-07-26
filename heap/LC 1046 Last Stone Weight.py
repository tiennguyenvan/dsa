class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        d_map = {}
        for x,y in points:
            d = math.sqrt(x ** 2 + y ** 2)
            # print((x,y), d)            
            if -d not in d_map:
                d_map[-d] = []
            d_map[-d].append([x,y])
            heapq.heappush(heap, -d)
            if len(heap) > k:
                heapq.heappop(heap)                
        ret = []
        # print(d_map)
        for _d in set(heap):
            ret.extend(d_map[_d])

        return ret