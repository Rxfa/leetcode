class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if 0 <= len(nums) <= 1:
            return len(nums)
        numset = set(nums)
        longest_streak = 1
        for num in nums:
            if num in numset:
                prev_num = num - 1
                next_num = num + 1
                current_streak = 1
                while prev_num in numset:
                    numset.remove(prev_num)
                    prev_num -= 1
                    current_streak += 1
                while next_num in numset:
                    numset.remove(next_num)
                    next_num += 1
                    current_streak += 1

                numset.remove(num)
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
