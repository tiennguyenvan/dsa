class Solution:
    def balancedString(self, s: str) -> int:
        s_len = len(s)
        chars_count = Counter(s)
        balance = s_len // 4
        def replaceable():            
            for ch in chars_count:
                if chars_count[ch] > balance:
                    return False
            return True

        if replaceable(): return 0
        ret = s_len        
        left = 0        

        for right in range(s_len):
            chars_count[s[right]] -= 1                        
            while left <= right and replaceable():
                ret = min(ret, right + 1 - left)                
                chars_count[s[left]] += 1
                left += 1                
        return ret