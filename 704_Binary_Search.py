class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        if target > nums[right] or target < nums[left]:
            return -1
        while left < right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
            
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1