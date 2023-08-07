# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list) -> None:
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def __str__(self) -> str:
        string = f"{self.title} ({self.seasons} seasons)\ngenres: "
        string += ", ".join(self.genres)
        if len(self.ratings) == 0:
            string += "\nno ratings"
        else:
            avg = sum(self.ratings) / len(self.ratings)
            string += f"\n{len(self.ratings)} ratings, average {avg:.1f} points"
        return string


def minimum_grade(rating: float, series_list: list):
    series_minimum = []
    for i in series_list:
        avg = sum(i.ratings) / len(i.ratings)
        if avg > rating:
            series_minimum.append(i)
    return series_minimum


def includes_genre(genre: str, series_list: list):
    series_genre = []
    for i in series_list:
        if genre in i.genres:
            series_genre.append(i)
    return series_genre


if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
