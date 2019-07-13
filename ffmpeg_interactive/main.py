import msvcrt
import os
import subprocess
import sys

from ffmpeg_args import make_ffmpeg_args
from util import split_path


def run():
    in_file = sys.argv[1]
    from_time = input('Cut from (HH:MM:SS.xxx): ')
    to_time = input('Cut to (may be blank):   ')
    out_file = input('Output file name:        ')

    # cd, so we don't end up in system32...
    working_dir, _ = split_path(in_file)
    os.chdir(working_dir)

    args = make_ffmpeg_args(in_file, out_file, from_time, to_time)
    p = subprocess.Popen(' '.join(args))
    p.wait()

    print('\nPress any key to continue...')
    msvcrt.getch()


if __name__ == '__main__':
    run()
