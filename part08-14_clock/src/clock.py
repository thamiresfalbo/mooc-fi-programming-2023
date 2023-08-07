# Write your solution here:
class Clock:
    def __init__(self, hour: int, minutes: int, seconds: int) -> None:
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.minutes == 59 and self.seconds == 59 and self.hour == 23:
            self.hour = 0
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

    def set(self, hour: int, minutes: int):
        self.hour = hour
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        return f"{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
