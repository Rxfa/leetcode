class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matchings = 0
        trainer_idx = 0
        player_idx = 0
        while player_idx < len(players) and trainer_idx < len(trainers):
            if players[player_idx] <= trainers[trainer_idx]:
                matchings += 1
                player_idx += 1
            trainer_idx += 1
        return matchings
