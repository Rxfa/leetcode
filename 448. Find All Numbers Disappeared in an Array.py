class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        max_n = len(nums) + 1
        nums = set(nums)
        for i in range(1, max_n):
            if i not in nums:
                res.append(i)
        return res