class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        pos = 0
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] < 3:
                nums[pos] = nums[i]
                pos += 1
        return pos