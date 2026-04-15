class MinStack:
    def __init__(self):
        self._data = []

    def push(self, val: int) -> None:
        self._data.append(val)

    def pop(self) -> None:
        self._data.pop()

    def top(self) -> int:
        return self._data[-1]

    def getMin(self) -> int:
        return min(self._data)
