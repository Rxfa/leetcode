class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= (i + 1)
        for i in nums:
            ans ^= i
        return ans
        