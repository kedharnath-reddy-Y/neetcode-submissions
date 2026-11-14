class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=set()
        s=set(nums1)
        for num in nums2:
            if num in s:
                ans.add(num)
        return list(ans)

        