class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        cars.sort(reverse=True, key=lambda x: x[0])
        
        fleets = 0
        last_time = 0
        
        for _, time in cars:
            if time > last_time:
                fleets += 1
                last_time = time
        return fleets