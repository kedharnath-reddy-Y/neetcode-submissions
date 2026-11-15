class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq={}
        ans=[]
        for arr in arr1:
            freq[arr]=freq.get(arr,0)+1
        for i in range(len(arr2)):
            if arr2[i] in freq:
                count=freq[arr2[i]]
                ans.extend([arr2[i]]*count)
                del freq[arr2[i]]
        for num in sorted(freq):
            ans.extend([num]*freq[num])
        return ans


        