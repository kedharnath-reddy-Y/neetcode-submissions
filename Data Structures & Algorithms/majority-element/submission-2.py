class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=defaultdict(int)
        res=MaxCount=0
        for num in nums:
            count[num]+=1
            if MaxCount<count[num]:
                res=num
                MaxCount=count[num]
        return res
        