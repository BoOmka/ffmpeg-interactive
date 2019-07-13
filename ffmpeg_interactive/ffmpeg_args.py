import typing as t

from util import add_extension, format_time, format_timedelta, get_duration, parse_time, split_path, get_extension


# Keys are for sorting (the least is the first)
DEFAULT_ARGS = {
    0: 'ffmpeg',
    1: '-hide_banner',
    40: '-c copy',
}

START_STR = '0:00:00.000'
END_STR = 'end'


def make_ffmpeg_args(in_file: str, out_file: str, from_time: str, to_time: str) -> t.Tuple[str, ...]:
    args = DEFAULT_ARGS.copy()

    from_time = parse_time(from_time)
    from_time_formatted = format_time(from_time)
    args[10] = f'-ss {from_time_formatted}'

    args[20] = f'-i "{in_file}"'

    try:
        to_time = parse_time(to_time)
    except ValueError:
        pass
    else:
        duration_formatted = format_timedelta(get_duration(from_time, to_time))
        args[30] = f'-to {duration_formatted}'

    _, in_file_name = split_path(in_file)
    in_file_extension = get_extension(in_file_name)
    args[50] = f'"{add_extension(out_file, extension=in_file_extension)}"'

    sorted_args = tuple(v for _, v in sorted(args.items()))

    return sorted_args
