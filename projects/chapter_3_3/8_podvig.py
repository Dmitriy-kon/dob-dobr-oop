from datetime import datetime


class DeltaClock:
    def __init__(self, clock1, clock2) -> None:
        self.clock1 = clock1
        self.clock2 = clock2
    
    def __str__(self) -> str:
        res = len(self)
        return datetime.fromtimestamp(res).strftime("%H: %M: %S")
    
    def __len__(self):
        res = self.clock1.get_time() - self.clock2.get_time()
        return res if res > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
