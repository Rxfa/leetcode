class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = {}
        if k < 1:
            return False
        for idx, num in enumerate(nums):
            if num in count and abs(count[num] - idx) <= k:
                return True
            count[num] = idx
        return False
