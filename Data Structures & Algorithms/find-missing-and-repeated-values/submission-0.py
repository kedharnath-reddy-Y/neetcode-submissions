class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        n=len(grid)
        missing,repeat=0,0
        for i in range(1,n*n+1):
            if freq.get(i,0)==2:
                repeat=i
            elif freq.get(i,0)==0:
                missing =i
        return [repeat,missing]