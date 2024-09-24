class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(0)
            else:
                prefix.append(prefix[-1] + nums[i-1])
        
        suffix = deque([])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suffix.appendleft(0)
            else:
                suffix.appendleft(suffix[0] + nums[i+1])


        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i

        return -1
