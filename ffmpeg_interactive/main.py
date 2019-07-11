import msvcrt
import os
import subprocess
import sys

from util import (
    add_extension,
    format_time,
    format_timedelta,
    get_duration,
    parse_time,
    split_path,
)


# Keys are for sorting (the least is the first)
DEFAULT_ARGS = {
    0: 'ffmpeg',
    40: '-c copy',
}


def make_args(in_file: str, out_file: str, from_time: str, to_time: str):
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


def run():
    in_file = sys.argv[1]
    from_time = input('Cut from (HH:MM:SS.xxx): ')
    to_time = input('Cut to (may be blank):   ')
    out_file = input('Output file name:        ')

    # cd, so we don't end up in system32...
    working_dir, _ = split_path(in_file)
    os.chdir(working_dir)

    args = make_args(in_file, out_file, from_time, to_time)
    p = subprocess.Popen(' '.join(args))
    p.wait()

    print('\nPress any key to continue...')
    msvcrt.getch()


if __name__ == '__main__':
    run()
