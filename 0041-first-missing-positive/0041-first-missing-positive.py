class Solution:
    def firstMissingPositive(self, nums):

        n = len(nums)

        # Put every number in its correct position
        for i in range(n):

            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find first wrong position
        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1