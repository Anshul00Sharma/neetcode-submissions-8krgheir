class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            self.store[key].append((value,timestamp))
        else:
            self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            # binary search
            if len(self.store[key]) < 1:
                return ""
            l,h = 0,len(self.store[key]) - 1
            arr = self.store[key]
            res = ""
            while l <= h:
                m = (l + h) // 2
                if arr[m][1] <= timestamp:
                    res = arr[m][0]
                    l = m + 1
                else:
                    h = m - 1
            return res
        else:
            return ""