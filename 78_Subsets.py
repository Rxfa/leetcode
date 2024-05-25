class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            current_subsets = subsets[:]
            for subset in current_subsets:
                subsets.append(subset + [i])
        return subsets
