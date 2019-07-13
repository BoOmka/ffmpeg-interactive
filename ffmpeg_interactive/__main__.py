import msvcrt
import os
import subprocess

import click

from ffmpeg_args import make_ffmpeg_args, START_STR, END_STR
from util import split_path


@click.command()
@click.argument('in_file', type=click.STRING)
@click.option('--from-time', type=click.STRING, prompt='Cut from', default=START_STR, show_default=START_STR,
              help='Time to cut from (HH:MM:SS.xxx')
@click.option('--to-time', type=click.STRING, prompt='Cut to', default=END_STR, show_default=END_STR,
              help='Time to cut to (HH:MM:SS.xxx')
@click.option('--out-file', type=click.STRING, prompt='Output filename', default=lambda: 'output',
              show_default='"output"', help='Output file name')
def run(in_file: str, from_time: str, to_time: str, out_file: str):
    # cd, so we don't end up in system32...
    working_dir, _ = split_path(in_file)
    os.chdir(working_dir)

    args = make_ffmpeg_args(in_file, out_file, from_time, to_time)
    p = subprocess.Popen(' '.join(args))
    p.wait()

    click.echo('Press any key to continue...')
    msvcrt.getch()


if __name__ == '__main__':
    run()
