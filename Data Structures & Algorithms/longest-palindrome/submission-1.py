class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen=set()
        res=0
        for ch in s:
            if ch in seen:
                seen.remove(ch)
                res+=2
            else:
                seen.add(ch)
        return res + 1 if seen else res
        