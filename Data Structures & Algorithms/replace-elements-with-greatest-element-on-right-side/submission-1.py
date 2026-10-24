class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maxEle=-1
        for i in range(n-1,-1,-1):
            curr=arr[i]
            arr[i]=maxEle
            maxEle=max(maxEle,curr)
        return arr