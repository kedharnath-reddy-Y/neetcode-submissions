class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[0]*n
        for i in range(n):
            maxEle=-1
            for j in range(i+1,n):
                maxEle=max(maxEle,arr[j])
            ans[i]=maxEle
        return ans

        