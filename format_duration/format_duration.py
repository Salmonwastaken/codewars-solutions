# https://www.codewars.com/kata/52742f58faf5485cae000b9a
from math import floor


# Timeframes in seconds
timeframes = {
    "year": 31536000,
    "day": 86400,
    "hour": 3600,
    "minute": 60,
    "second": 1
    }


def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"

    frame_occurences = {}

    for frame, time in timeframes.items():
        occurences = floor((seconds / time))

        if occurences >= 1:
            frame_occurences[frame] = occurences
            seconds -= occurences * time

    try:
        and_key = list(frame_occurences)[-2]
        last = False
    except IndexError:
        and_key = None
        last = True

    result = ""
    for frame, occurences in frame_occurences.items():
        result += f"{occurences} {frame}"
        if occurences > 1:
            result += "s"
        if last is True:
            continue
        if and_key == frame:
            last = True
            result += " and "
            continue
        result += ", "

    return result
