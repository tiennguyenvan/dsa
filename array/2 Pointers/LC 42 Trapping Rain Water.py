class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        l = 0
        pre_l = l
        r = n - 1
        pre_r = r
        ret = 0
        def get_trap_water(i,j):            
            min_h = min(h[i], h[j])
            trap = 0
            for m in range(min(i,j)+1,max(i,j)):
                trap += min_h - h[m]
            # print(f"    Trapped btw: [{i}, {j}] trap={trap}")
            return trap

        while l < r:
            # print(f"Check l={l}, r={r}")            
            if h[l] < h[r]:
                l+=1                              
                # print(f"    Updated: l={l}")
                if h[l] >= h[pre_l]:
                    ret += get_trap_water(pre_l, l)
                    pre_l = l
            else:
                r-=1
                # print(f"    Updated: r={r}")
                if h[r] >= h[pre_r]:
                    ret += get_trap_water(pre_r, r)
                    pre_r = r                
            
                
            
            # print(f"    Ret Updated: {ret}")
            
        return ret