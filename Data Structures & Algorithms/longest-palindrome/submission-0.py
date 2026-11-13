class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        has_odd=False
        length=0
        for ch,count in freq.items():
            if count%2==0:
                length+=count
            else:
                has_odd=True
                length+=count-1
        if has_odd:
            return length+1
        return length


        