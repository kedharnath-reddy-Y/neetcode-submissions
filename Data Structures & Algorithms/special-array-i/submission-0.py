class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if nums[0] % 2 == 0:
            for i in range(0, len(nums), 2):
                if nums[i] % 2 != 0:
                    return False

            for i in range(1, len(nums), 2):
                if nums[i] % 2 == 0:
                    return False

        else:
            for i in range(0, len(nums), 2):
                if nums[i] % 2 == 0:
                    return False

            for i in range(1, len(nums), 2):
                if nums[i] % 2 != 0:
                    return False

        return True