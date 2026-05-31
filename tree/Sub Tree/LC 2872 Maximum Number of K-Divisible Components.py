class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        cons = {}
        for a,b in edges:
            if not a in cons:
                cons[a] = []
            if not b in cons:
                cons[b] = []
            cons[a].append(b)
            cons[b].append(a)
        # print(cons)
        ret = 0
        def sumVal(parent, root):
            nonlocal ret
            nonlocal k
            nonlocal cons
            nonlocal values
            # print(parent, root)            
            total = values[root]
            if root in cons:              
                for child in cons[root]:
                    if child == parent:
                        continue
                    total += sumVal(root, child)            
            if total % k == 0:
                ret+=1
                return 0
            # print(values[root], total)
            return total
        sumVal(None, 0)
        return ret