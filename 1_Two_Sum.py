class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, value in enumerate(nums):
            if target - value in d:
                return [d[target - value], idx]
            d[value] = idx
        