import datetime as dt

from dateutil import parser

from ffmpeg_interactive.util import add_missing_colons


def parse_time(time_str: str) -> dt.time:
    time_str = add_missing_colons(time_str)
    dt_obj = parser.parse(time_str)
    return dt_obj.time()
