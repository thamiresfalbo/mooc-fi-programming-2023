# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, maximum_weight: int) -> None:
        self.maximum_weight = maximum_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() > self.maximum_weight:
            return
        self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        heavy = Item("", 0)
        for item in self.__items:
            if item.weight() > heavy.weight():
                heavy = item
        return heavy

    def weight(self):
        a = 0
        for i in self.__items:
            a += i.weight()
        return a

    def __str__(self) -> str:
        if len(self.__items) == 1:
            return f"1 item ({self.__items[0].weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"


class CargoHold:
    def __init__(self, maximum_weight: int) -> None:
        self._maximum_weight = maximum_weight
        self.__suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() > self._maximum_weight:
            return
        else:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def weight(self):
        w = 0
        for suitcase in self.__suitcases:
            w += suitcase.weight()
        return w

    def __str__(self) -> str:
        amount = len(self.__suitcases)
        space = self._maximum_weight - self.weight()
        if len(self.__suitcases) == 1:
            return f"{amount} suitcase, space for {space} kg"
        else:
            return f"{amount} suitcases, space for {space} kg"


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")
