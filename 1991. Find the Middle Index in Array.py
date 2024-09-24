class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return idx
            left_sum += num
        return -1