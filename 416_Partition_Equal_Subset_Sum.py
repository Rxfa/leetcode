class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 or not nums:
            return False
        memo = {0}
        target = sum(nums) / 2
        for i in nums:
            memo2 = set()
            for j in memo:
                if j + i == target or j == target:
                    return True
                if j + i < target:
                    memo2.add(j + i)
                if j < target:
                    memo2.add(j)
            memo = memo2
        return target in memo