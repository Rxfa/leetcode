class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            low, high = i + 1, len(nums) - 1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum  - target) < abs(closest - target):
                    closest = curr_sum
                if curr_sum > target:
                    high -= 1
                else:
                    low += 1
        return closest
