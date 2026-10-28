class Solution:
    def maxDifference(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        arr=list(freq.values())
        even,odd=[],[]
        for num in arr:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort(reverse=True)
        return odd[0]-even[0]