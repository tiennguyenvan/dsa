class Solution:
    def hash(self, word:str) -> str:
        key = [0]*26
        for code in word.encode():
            key[code - ord('a')] += 1
        return ','.join(map(str,key))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed_words = {}
        for word in strs:            
            word_hash = self.hash(word)
            # print(f"word={word}, hash={word_hash}")
            if word_hash not in hashed_words:
                hashed_words[word_hash] = []
            hashed_words[word_hash].append(word)
        return [group for group in hashed_words.values()]