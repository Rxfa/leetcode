class Solution:
    def numberOfSubarrays(nums: List[int], k: int) -> int:
        def atMostK(k: int) -> int:
            count = 0
            left = 0
            odd_count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                count += right - left + 1
            return count
        
        return atMostK(k) - atMostK(k - 1)


