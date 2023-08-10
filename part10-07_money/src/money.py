# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        money = f"{float(self.__euros + (self.__cents / 100)):.2f}"
        return f"{money} eur"

    def __eq__(self, another) -> bool:
        return self.__str__() == another.__str__()

    def __lt__(self, another) -> bool:
        return self.__str__() < another.__str__()

    def __gt__(self, another) -> bool:
        return self.__str__() > another.__str__()

    def __ne__(self, another) -> bool:
        return self.__str__() != another.__str__()

    def __add__(self, another):
        a = self.__euros + another.__euros
        b = self.__cents + another.__cents
        return Money(a, b)

    def __sub__(self, another):
        a = self.__euros - another.__euros
        b = self.__cents - another.__cents
        z = float(a + (b / 100))
        if z < 0:
            raise ValueError
        return Money(a, b)
