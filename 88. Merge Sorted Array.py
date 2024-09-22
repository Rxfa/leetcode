class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = nums1[:m]
        pointer1 = pointer2 = 0
        for i in range(len(nums1)):
            if pointer1 < m and (pointer2 >= n or arr[pointer1] <= nums2[pointer2]):
                nums1[i] = arr[pointer1]
                pointer1 += 1
            else:
                nums1[i] = nums2[pointer2]
                pointer2 += 1
