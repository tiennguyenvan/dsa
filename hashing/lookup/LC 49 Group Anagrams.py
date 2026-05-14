class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashId(s):
            sMap = [0]*26
            for c in s:                
                sMap[ord(c)-ord('a')] += 1
            return ','.join(map(str,sMap))

        sMap = {}
        for s in strs:
            sid = hashId(s)
            if sid not in sMap:
                sMap[sid] = []
            sMap[sid].append(s)
            # print(s, sid, sMap)
        return list(sMap.values())
