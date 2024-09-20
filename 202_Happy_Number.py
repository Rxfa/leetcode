class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, num):
        ans = 0
        while num > 0:
            ans += (num % 10) ** 2
            num = num // 10
        return ans
