class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        k = 0
        while idx < len(nums):
            if nums[idx] == val:
                k += 1
                nums[idx] = -1
            idx += 1
        nums.sort(reverse=True)
        return len(nums) - k
