class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        lucky=0
        maxLuck=0
        for num,count in freq.items():
            if num==count:
                lucky=num
                maxLuck=max(lucky,maxLuck)
        if maxLuck==0:
            return -1
        else:
            return maxLuck

        