from util import add_extension, format_time, format_timedelta, get_duration, parse_time


# Keys are for sorting (the least is the first)
DEFAULT_ARGS = {
    0: 'ffmpeg',
    40: '-c copy',
}


def make_ffmpeg_args(in_file: str, out_file: str, from_time: str, to_time: str):
    args = DEFAULT_ARGS.copy()

    from_time = parse_time(from_time)
    from_time_formatted = format_time(from_time)
    args[10] = f'-ss {from_time_formatted}'

    args[20] = f'-i "{in_file}"'

    try:
        to_time = parse_time(to_time)
    except ValueError:
        to_time = None
    if to_time:
        duration_formatted = format_timedelta(get_duration(from_time, to_time))
        args[30] = f'-to {duration_formatted}'

    args[50] = f'"{add_extension(out_file)}"'

    sorted_args = tuple(v for _, v in sorted(args.items()))

    return sorted_args