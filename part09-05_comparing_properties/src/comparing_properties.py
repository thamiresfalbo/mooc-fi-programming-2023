# Write your solution here:


class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to):
        a = self.price_per_sqm * self.square_metres
        b = compared_to.price_per_sqm * compared_to.square_metres
        if a - b < 0:
            return b - a
        return a - b

    def more_expensive(self, compared_to):
        a = self.price_per_sqm * self.square_metres
        b = compared_to.price_per_sqm * compared_to.square_metres
        return a > b
