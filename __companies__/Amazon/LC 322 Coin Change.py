class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        limit = 100
        def minNumCoinTarget(target: int) -> int:
            if target in memo:
                return memo[target]
            if target < 0:
                return -1
            if target == 0:
                return 0
            
            minNumCoin = float("inf")
            for c in coins:
                n = minNumCoinTarget(target - c)
                if n == -1:
                    continue
                minNumCoin = min(minNumCoin, n)

            memo[target] = -1 if minNumCoin == float("inf") else minNumCoin + 1
            return memo[target]
        return minNumCoinTarget(amount)