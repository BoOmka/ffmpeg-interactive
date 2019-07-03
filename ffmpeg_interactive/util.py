import datetime as dt


VIDEO_EXTENSIONS = {'mp4', 'avi', 'wmv', 'mkv', }
DEFAULT_EXTENSION = 'mp4'


def add_extension(filename: str) -> str:
    if filename.split('.')[-1] in VIDEO_EXTENSIONS:
        return filename
    return f'{filename}.{DEFAULT_EXTENSION}'


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
        raise ValueError('Duration must be positive')
    return dt.timedelta(seconds=duration_seconds)
