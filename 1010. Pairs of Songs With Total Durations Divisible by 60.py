class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        pairs = 0
        for song in time:
            duration = song % 60
            count[duration] += 1
        pairs += (count[0] * (count[0] - 1)) // 2
        for key in range(1, 30):
            pairs += count[key] * count[60 - key]
        pairs += (count[30] * (count[30] - 1)) // 2
        return pairs
