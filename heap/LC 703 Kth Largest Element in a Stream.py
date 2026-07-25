class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kLargestScores = []
        self.k = k        
        for n in nums:
            heapq.heappush(self.kLargestScores, n)
        self.__sizing()

    def __sizing(self):
        while len(self.kLargestScores) > self.k:
            heapq.heappop(self.kLargestScores)

    def add(self, val: int) -> int:
        heapq.heappush(self.kLargestScores, val)
        self.__sizing()
        return self.kLargestScores[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
