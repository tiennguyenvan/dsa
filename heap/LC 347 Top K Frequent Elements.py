class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        v2f = Counter(nums)
        f2v = {}
        for v in nums:
            f = v2f[v]
            if f not in f2v:
                f2v[f] = set()
            f2v[f].add(v)
        sorted_f = sorted(f2v.keys(), reverse = True)
        ret = []
        # print(f"nums = {nums}, v2f = {v2f}, f2v = {f2v}, sorted_f = {sorted_f}")
        for f in sorted_f:            
            for v in f2v[f]:
                ret.append(v)
                if len(ret) == k:
                    return ret


        return ret


        