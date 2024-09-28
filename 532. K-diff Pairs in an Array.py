class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        if k == 0:
            count = Counter(nums)
            for i in count.values():
                if i > 1:
                    pairs += 1
            return pairs
        
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    pairs += 1
                    break
        return pairs