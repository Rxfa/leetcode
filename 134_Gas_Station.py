class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        def travel(start):
            tank = 0
            for i in range(n):
                idx = (start + i) % n
                tank += gas[idx] - cost[idx]
                if tank < 0:
                    return False
            return True
        for idx in range(n):
            if travel(idx):
                return idx
        return -1
