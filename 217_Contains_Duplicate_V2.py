class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) <= 1:
            return False

        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
