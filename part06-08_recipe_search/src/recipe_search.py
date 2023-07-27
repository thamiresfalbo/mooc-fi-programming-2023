# Write your solution here
def load_recipes(filename: str):
    recipes_list = []
    one_recipe = []

    with open(filename) as file:
        for line in file:
            if line != "\n":
                one_recipe.append(line.strip())
            else:
                recipes_list.append(one_recipe)
                one_recipe = []
        recipes_list.append(one_recipe)

    cookbook = {}
    for i in recipes_list:
        cookbook[i[0]] = i[1:]
    return cookbook


def search_by_name(filename: str, word: str):
    cookbook = load_recipes(filename=filename)

    found = []
    for recipes in cookbook.keys():
        if word in recipes.lower():
            found.append(recipes)
            continue

    return found


def search_by_time(filename: str, prep_time: int):
    cookbook = load_recipes(filename=filename)
    found = []
    for recipe in cookbook.items():
        if int(recipe[1][0]) <= prep_time:
            found.append(f"{recipe[0]}, preparation time {recipe[1][0]} min")
    return found


def search_by_ingredient(filename: str, ingredient: str):
    cookbook = load_recipes(filename=filename)
    found = []
    for recipe in cookbook.items():
        if ingredient in recipe[1]:
            found.append(f"{recipe[0]}, preparation time {recipe[1][0]} min")
    return found


if __name__ == "__main__":
    search_by_name("recipes1.txt", "cake")
    some_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for i in some_recipes:
        print(i)
