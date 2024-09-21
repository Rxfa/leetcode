class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pointer = len(arr) - 2
        biggest = arr[-1]
        res = [-1 for _ in arr]
        while pointer >= 0:
            biggest = max(biggest, arr[pointer + 1])
            res[pointer] = biggest
            pointer -= 1
        return res
