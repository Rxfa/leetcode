class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            found = False
            index = nums2.index(num)
            
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                    break
            
            if not found:
                result.append(-1)
        
        return result
