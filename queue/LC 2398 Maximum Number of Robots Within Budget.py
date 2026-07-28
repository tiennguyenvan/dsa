class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:        
        curTotalCost = 0
        left = 0
        maxLen = 0
        maxTimes = deque()
        
        for right,time in enumerate(chargeTimes):
            cost = runningCosts[right]            
            # print(f"{left}->{right} {time}+{cost}={time+cost} max:{maxTimes[0][1] if maxTimes else None} total:{curTotalCost} len:{maxLen} -> {maxTimes}")

            # process the new max time if adding this robot
            curTotalCost -= maxTimes[0][1] if maxTimes else 0
            while maxTimes and maxTimes[-1][1] <= time:
                maxTimes.pop()
            maxTimes.append((right,time,cost))
            k = right - left
            curTotalCost = curTotalCost // (k if k else 1)
            curTotalCost += cost
            curTotalCost *= (k + 1)
            curTotalCost += maxTimes[0][1]
            # print(f"    processed k:{k} total:{curTotalCost} max:{maxTimes[0][1]} -> {maxTimes}")


            # recorrect left to fit the budget
            while maxTimes and left <= right and curTotalCost > budget:
                k = right - left + 1
                curTotalCost -= maxTimes[0][1]                
                curTotalCost = curTotalCost // k
                curTotalCost -= runningCosts[left]                

                if left == maxTimes[0][0]:                    
                    maxTimes.popleft()                                    
                left += 1
                k = right - left + 1                            
                curTotalCost *= k
                curTotalCost += (maxTimes[0][1] if maxTimes else 0)
            
            # curTotalCost fits to the budget
            maxLen = max(maxLen, right - left + 1)

            # print(f"    final total:{curTotalCost} len:{maxLen} max:{maxTimes[0][1] if maxTimes else None} -> {maxTimes}\n")

        return maxLen
                
            
            
            





