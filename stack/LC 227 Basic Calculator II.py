class Solution:
    def calculate(self, s: str) -> int:
        ret = []                
        cleaned = re.split(r"\s*([-+*/])\s*", s.strip())
        stack = []
        for e in cleaned:
            if not stack or (stack[-1] not in ['*', '/']):
                stack.append(e)
                continue
            last = stack.pop()
            stack[-1] = int(stack[-1]) // int(e) if last == '/' else int(stack[-1]) * int(e)
        for e in stack:
            if not ret or (ret[-1] not in ['+', '-']):
                ret.append(e)
                continue
            last = ret.pop()
            ret[-1] = int(ret[-1]) + int(e) if last == '+' else int(ret[-1]) - int(e)
        
        return int(ret[0])

                