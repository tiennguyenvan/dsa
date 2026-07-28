class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set  = set()
        for endStr in deadends:
            end = tuple(map(int, endStr))
            dead_set.add(end)
        target_list = tuple(map(int, target))
        if target_list in dead_set: return -1
        start = (0,0,0,0)
        if target_list == start: return 0
        if start in dead_set: return -1
        q = deque()
        q.append(start)
        modifiers = [-1,1]
        visited = set()
        visited.add(start)
        lvl = 0
        while len(q):
            l = len(q)
            lvl +=1
            for _ in range(l):
                cur = q.popleft()
                for i in range(4):
                    for m in modifiers:
                        new_list = list(cur)
                        new_list[i] += m 
                        if new_list[i] < 0: new_list[i] = 9
                        elif new_list[i] > 9: new_list[i] = 0
                        new_list = tuple(new_list)
                        if new_list in visited: continue
                        visited.add(new_list)
                        if new_list in dead_set: continue
                        if new_list == target_list: 
                            return lvl
                        q.append(new_list)

        return -1


                    
