class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s1 = Counter()     
        for i,w in enumerate(list1):
            s1[w] = i        
        s2 = Counter()
        for i,w in enumerate(list2):
            s2[w] = i
        s = Counter()
        for w in s1:
            if w not in s2:
                continue
            s[w] = s1[w] + s2[w]
        minW = float('inf')
        ret = []
        for w in s:
            if s[w] < minW:
                ret = []
                ret.append(w)
                minW = s[w]
                continue
            if s[w] > minW:
                continue
            ret.append(w)

        return ret