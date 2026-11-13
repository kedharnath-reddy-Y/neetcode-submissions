class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq={}
        for word in words:
            for ch in word:
                freq[ch]=freq.get(ch,0)+1
        for ch,count in freq.items():
            if count%len(words)!=0:
                return False
        return True


        