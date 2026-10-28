class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        idx,res=[],[-1]*len(nums1)
        greaterEle=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    idx.append(j)
        for i in range(len(nums1)):
            
            for j in range(idx[i]+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    res[i]=nums2[j] 
                    break
        return res  
                  