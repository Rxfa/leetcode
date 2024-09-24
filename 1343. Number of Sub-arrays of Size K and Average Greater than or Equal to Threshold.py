class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arr.append(0)
        curr_sum = sum(arr[:k])
        subarrays = 0
        for i in range(k, len(arr)):
            if (curr_sum / k) >= threshold:
                subarrays += 1
            curr_sum -= arr[i-k]
            curr_sum += arr[i]
        return subarrays
