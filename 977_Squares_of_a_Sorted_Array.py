class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = deque()
        left, right = 0, len(nums) - 1
        while left <= right:
            squared_l, squared_r = nums[left] ** 2, nums[right] ** 2
            if squared_l > squared_r:
                arr.appendleft(squared_l)
                left += 1
            else:
                arr.appendleft(squared_r)
                right -= 1
        return arr
