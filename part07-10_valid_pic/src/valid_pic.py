# Write your solution here
from datetime import datetime, timedelta


def is_it_valid(pic: str) -> bool:
    CONTROL_STRING = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    CENTURY_DICT = {"+": 1800, "-": 1900, "A": 2000}

    # Check pic length
    if len(pic) > 11:
        return False

    # The format is ddmmyyXyyyZ
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    century = pic[6]
    control_character = pic[10]

    try:
        numbers = int(pic[0:6] + pic[7:10]) % 31
        # Check century marker and control character
        if (
            century not in CENTURY_DICT.keys()
            or CONTROL_STRING[numbers] != control_character
        ):
            return False

        year += CENTURY_DICT[century]

        # Check date is valid
        datetime(year, month, day)

        return True
    except:
        return False


if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
