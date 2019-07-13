import datetime as dt
import re

from dateutil import parser

import exceptions


VIDEO_EXTENSIONS = {'mp4', 'avi', 'wmv', 'mkv', }
DEFAULT_EXTENSION = 'mp4'
WINDOWS_PATH_RE = re.compile(r"^[a-zA-Z]:\\(((?![<>:\"/\\|?*]).)+((?<![ .])\\)?)*$")


def get_extension(filename: str) -> str:
    separated_name = filename.rsplit('.', maxsplit=1)
    if len(separated_name) > 1:
        return separated_name[-1]
    else:
        return ''


def add_extension(filename: str, extension: str = DEFAULT_EXTENSION) -> str:
    extension = extension or DEFAULT_EXTENSION
    if filename.split('.')[-1] in VIDEO_EXTENSIONS:
        return filename
    return f'{filename}.{extension}'


def add_missing_colons(time_str: str) -> str:
    colons = time_str.count(':')
    return f'{"00:" * (2 - colons)}{time_str}'


def format_time(time: dt.time) -> str:
    return time.strftime('%H:%M:%S.%f')[:-3]


def timedelta_to_time(timedelta: dt.timedelta) -> dt.time:
    return (dt.datetime.min + timedelta).time()


def format_timedelta(timedelta: dt.timedelta) -> str:
    return format_time(timedelta_to_time(timedelta))


def time_to_float(time: dt.time) -> float:
    return time.hour * 3600 + time.minute * 60 + time.second + time.microsecond / 1e6


def get_duration(start_time: dt.time, end_time: dt.time) -> dt.timedelta:
    duration_seconds = time_to_float(end_time) - time_to_float(start_time)
    if duration_seconds <= 0:
        raise exceptions.WrongDurationError()
    return dt.timedelta(seconds=duration_seconds)


def parse_time(time_str: str) -> dt.time:
    time_str = add_missing_colons(time_str)
    dt_obj = parser.parse(time_str)
    return dt_obj.time()


def split_path(path: str) -> (str, str):
    """Return path to directory and file name"""
    path = path.replace('/', '\\')
    try:
        dir_path, filename = path.rsplit('\\', maxsplit=1)
    except ValueError:
        raise ValueError(
            'path must be valid absolute file path '
            '(i.e. starting with drive letter and ending with file name)'
        )
    return dir_path, filename
