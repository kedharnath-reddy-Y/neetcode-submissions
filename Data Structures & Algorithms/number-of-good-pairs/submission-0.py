class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        pairs = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for count in freq.values():
            pairs += (count * (count - 1)) // 2

        return pairs