class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = dict()
            self.timestamps[key] = []
        self.store[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        if timestamp in self.store[key]:
            return self.store[key][timestamp]
        curr_timestamp = len(self.timestamps[key]) - 1
        while self.timestamps[key][curr_timestamp] > timestamp:
            curr_timestamp -= 1
            if curr_timestamp < 0:
                return ""
        return self.store[key][self.timestamps[key][curr_timestamp]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
