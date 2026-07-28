class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = deque()
        while deck:
            if result:
                result.append(result.popleft())
            result.append(deck.pop())        
        result = list(result)        
        result.reverse()        
        return result