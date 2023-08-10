# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


# If the password argument given to either of these methods is wrong,
# the methods should raise a ValueError exception.
# If the password is correct, each method should call the relevant
# method in the parent class. Do not copy and paste anything from the MagicPotion class.


# An example of how this would work:
class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        super().__init__(name)
        self._password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password != self._password:
            raise ValueError
        super().add_ingredient(ingredient, amount)

    def print_recipe(self, password: str):
        if password != self._password:
            raise ValueError
        super().print_recipe()


if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus")  # WRONG password!
