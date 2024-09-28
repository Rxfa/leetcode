class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        arr = list(count.keys())
        arr.sort()
        res = 0
        mod = 10**9 + 7
        for i in range(len(arr)):
            j, k = i, len(arr) - 1
            while i <= j <= k:
                if (arr[j] + arr[k]) > (target - arr[i]):
                    k -= 1
                elif (arr[j] + arr[k]) < (target - arr[i]):
                    j += 1
                else:
                    if i == j == k:
                        res += count[arr[i]] * (count[arr[i]] - 1) * (count[arr[i]] - 2) // 6
                    elif i == j:
                        res += count[arr[i]] * (count[arr[i]] - 1) // 2 * count[arr[k]]
                    elif j == k:
                        res += count[arr[j]] * (count[arr[j]] - 1) // 2 * count[arr[i]]
                    else:
                        res += count[arr[i]] * count[arr[j]] * count[arr[k]]
                    res %= mod
                    j += 1
                    k -= 1
        return res
