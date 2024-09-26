class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        sum_count_map = {0: 1}
        count = 0
        
        for num in nums:
            cumulative_sum += num 
            
            if cumulative_sum - k in sum_count_map:
                count += sum_count_map[cumulative_sum - k]
            
            if cumulative_sum in sum_count_map:
                sum_count_map[cumulative_sum] += 1
            else:
                sum_count_map[cumulative_sum] = 1
        return count
