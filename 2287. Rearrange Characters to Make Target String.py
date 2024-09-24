class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        target = Counter(target)
        reps = 0
        while True:
            for key, val in target.items():
                if counter.get(key, -1) < val:
                    return reps
                counter[key] -= val
            reps += 1