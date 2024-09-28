class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def houseRobber(arr):
            if len(arr) == 1:
                return arr[0]
            if len(arr) < 3:
                return max(arr[-1], arr[0])
            arr[2] += arr[0]            
            for i in range(3, len(arr)):
                arr[i] += max(arr[i-2], arr[i-3])
            return max(arr[-1], arr[-2])
            
        return max(houseRobber(nums[:len(nums)-1]), houseRobber(nums[1:]))