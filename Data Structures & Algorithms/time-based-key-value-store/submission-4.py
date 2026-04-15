class TimeMap:
    def __init__(self):
        self.d = {}
        self.keys_timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        array = self.d[key]
        if len(array) == 0:
            return ""
        l = 0
        r = len(array) - 1
        while l <= r:
            middle = (l + r ) // 2
            if array[middle][0] == timestamp:
                return array[middle][1]
            elif array[middle][0] < timestamp:
                l = middle + 1
            else:
                r = middle - 1
        if array[r][0] < timestamp:
            return array[r][1]
        return ""