# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 00
        self.minutes = 00

    def tick(self):
        if self.seconds == 59 and self.minutes == 59:
            self.minutes = 0
            self.seconds = 0
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
        else:
            self.seconds += 1

    def __str__(self) -> str:
        return f"{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()
