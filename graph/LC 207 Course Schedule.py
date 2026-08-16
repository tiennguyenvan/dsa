class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:                
        reqMap = {}
        for a,b in prerequisites:            
            if a not in reqMap:
                reqMap[a] = set()
            reqMap[a].add(b)        
        took = set()

        def canTake(c:int, deps):
            if c not in reqMap or c in took:
                return True

            if c in deps:
                return False
            deps.add(c)
            for p in reqMap[c]:
                if not canTake(p, deps):
                    return False    
            took.add(c)                
            return True

        for c in range(numCourses):            
            deps = set()
            if not canTake(c, deps):
                return False
            took.add(c)
        return True

            

        


