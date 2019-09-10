import pytest

from ffmpeg_args import make_ffmpeg_args


class TestMakeArgs:
    @pytest.mark.parametrize(
        'from_str, to_str, result_cmd',
        (
            (
                '00:04:55.123', '00:05:00.000',
                ('ffmpeg', '-hide_banner', '-ss 00:04:55.123', r'-i "C:\input.mp4"', '-to 00:00:04.877', '-c copy',
                 '"output.mp4"')
            ),
            (
                '00:04:55.123', '',
                ('ffmpeg', '-hide_banner', '-ss 00:04:55.123', r'-i "C:\input.mp4"', '-c copy', '"output.mp4"')
            ),
            (
                '00:04:55.123', 'lalala',
                ('ffmpeg', '-hide_banner', '-ss 00:04:55.123', r'-i "C:\input.mp4"', '-c copy', '"output.mp4"')
            ),
            (
                '10', '20',
                ('ffmpeg', '-hide_banner', '-ss 00:00:10.000', r'-i "C:\input.mp4"', '-to 00:00:10.000', '-c copy',
                 '"output.mp4"')
            ),
            (
                '10', '',
                ('ffmpeg', '-hide_banner', '-ss 00:00:10.000', r'-i "C:\input.mp4"', '-c copy', '"output.mp4"')
            ),
        )
    )
    def test_parametrized_times__returns_args(self, from_str, to_str, result_cmd):
        result = make_ffmpeg_args(r'C:\input.mp4', 'output.mp4', from_time=from_str, to_time=to_str)
        assert result == result_cmd

    @pytest.mark.parametrize(
        'from_str, to_str',
        (
            ('00:00:00:01', ''),
            ('3', '2'),
        )
    )
    def test_parametrized_times__raises_value_error(self, from_str, to_str):
        with pytest.raises(ValueError):
            make_ffmpeg_args(r'C:\input.mp4', 'output.mp4', from_time=from_str, to_time=to_str)

    def test_relative_infile_path__raises_value_error(self):
        with pytest.raises(ValueError):
            make_ffmpeg_args('input.mp4', 'output.mp4', from_time='00:04:55.123', to_time='00:05:00.000')