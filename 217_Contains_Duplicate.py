class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
