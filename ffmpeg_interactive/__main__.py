import msvcrt
import os
import subprocess
import typing as t

import click
import colorama

import exceptions
from ffmpeg_args import END_STR, make_ffmpeg_args, START_STR
from util import split_path, WINDOWS_PATH_RE


def validate_input_path(ctx, _, value):
    if WINDOWS_PATH_RE.match(value):
        return value
    else:
        click.echo('Wrong input file path')
        ctx.abort()


def echo_error(msg: t.Any) -> None:
    click.echo(colorama.Fore.RED + str(msg))


@click.command()
@click.argument('in_file', type=click.STRING, callback=validate_input_path)
@click.option('--from-time', type=click.STRING, prompt='Cut from', default=START_STR, show_default=START_STR,
              help='Time to cut from (HH:MM:SS.xxx')
@click.option('--to-time', type=click.STRING, prompt='Cut to', default=END_STR, show_default=END_STR,
              help='Time to cut to (HH:MM:SS.xxx')
@click.option('--out-file', type=click.STRING, prompt='Output filename', default='output', show_default='"output"',
              help='Output file name')
@click.option('--ffmpeg-params', type=click.STRING, prompt='Additional params', default='', show_default='',
              help='Additional ffmpeg params')
def run(in_file: str, from_time: str, to_time: str, out_file: str, ffmpeg_params: str):
    colorama.init()

    # cd, so we don't end up in system32...
    working_dir, _ = split_path(in_file)
    os.chdir(working_dir)

    try:
        args = make_ffmpeg_args(in_file, out_file, from_time, to_time)
    except exceptions.WrongDurationError as e:
        echo_error(e)
        exit(1)
    else:
        p = subprocess.Popen(' '.join(args) + ffmpeg_params)
        p.wait()

    click.echo('Press any key to continue...')
    msvcrt.getch()


if __name__ == '__main__':
    run()
