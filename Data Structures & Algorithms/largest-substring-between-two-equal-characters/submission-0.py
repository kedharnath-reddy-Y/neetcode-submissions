class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq={}
        max_len=-1
        for i,ch in enumerate(s):
            if ch not in freq:
                freq[ch]=i
            else:
                length=i-freq[ch]-1
                max_len=max(max_len,length)
        return max_len