class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        # init queue
        def appendToDq(i):
            # print(i, nums[i], ' => ', dq)
            if not dq:                
                dq.append(i)
                # print('out 1', dq)
                return
            while len(dq) == k:
                dq.popleft()
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            # print('out 2', dq)

        for i in range(k-1):            
            appendToDq(i)

        n = len(nums)
        ret = []
        for i in range(k-1, n):            
            appendToDq(i)
            
            ret.append(nums[dq[0]])
        return ret

