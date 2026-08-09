class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        curPop = 0
        for v in pushed:
            if not stack or stack[-1] != popped[curPop]:
                stack.append(v)
            while stack and stack[-1] == popped[curPop]:
                curPop += 1
                stack.pop()
        return curPop == len(popped)
            
