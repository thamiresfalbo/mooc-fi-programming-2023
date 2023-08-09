# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        if self.__petrol == 0:
            return
        self.__odometer += km
        self.__petrol -= km

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"
