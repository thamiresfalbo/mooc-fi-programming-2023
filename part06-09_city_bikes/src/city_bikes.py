# Write your solution here
import math


def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename) as f:
        for line in f:
            if "FID" in line:
                continue
            parts = line.split(";")
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict) -> tuple:
    pass


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
