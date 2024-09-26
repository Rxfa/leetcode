class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            low, high = i + 1, len(nums) - 1
            while low766. Toeplitz Matrix

                    low += 1
        return closest
