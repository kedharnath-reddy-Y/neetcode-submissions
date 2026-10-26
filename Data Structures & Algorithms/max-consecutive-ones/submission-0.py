class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon=0
        con=0
        for num in nums:
            if num==1:
                con+=1            
            else:
                con=0
            maxCon=max(maxCon,con)
        return maxCon
        