class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def __str__(self):
        return f"{self._format_time(self._hours)}:{self._format_time(self._minutes)}:{self._format_time(self._seconds)}"

    def _format_time(self, time):
        return str(time).zfill(2)

    def next_second(self):
        self._seconds = (self._seconds + 1) % 60
        if self._seconds == 0:
            self._minutes = (self._minutes + 1) % 60
            if self._minutes == 0:
                self._hours = (self._hours + 1) % 24

    def prev_second(self):
        self._seconds = (self._seconds - 1) % 60
        if self._seconds == 59:
            self._minutes = (self._minutes - 1) % 60
            if self._minutes == 59:
                self._hours = (self._hours - 1) % 24


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)