class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for i in nums:
            apps = 1 + counter.get(i, 0)
            if apps > len(nums) // 2:
                return i
            counter[i] = apps
