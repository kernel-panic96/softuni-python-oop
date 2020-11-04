class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    mmax_hours = 24
    mmax_minutes = 60
    mmax_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hs, ms, ss):
        self.hours = hs
        self.minutes = ms
        self.seconds = ss

    def get_time(self):
        hh = str(self.hours).zfill(2)
        mm = str(self.minutes).zfill(2)
        ss = str(self.seconds).zfill(2)

        return f'{hh}:{mm}:{ss}'

    def next_second(self):
        self.seconds = (self.seconds + 1) % self.mmax_seconds
        self.minutes = (self.minutes + (self.seconds == 0)) % self.mmax_minutes
        self.hours = (self.hours + (self.minutes == 0)) % self.mmax_hours

        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())
print(time.get_time())
