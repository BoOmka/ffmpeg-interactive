import datetime

import freezegun
import pytest

from ffmpeg_interactive.util import add_missing_colons
from util import parse_time


class TestAddMissingColons:
    @pytest.mark.parametrize(
        'time_str, expected',
        (
            ('01:02:03', '01:02:03'),
            ('01:02', '00:01:02'),
            ('01', '00:00:01'),
            ('01:02:03:04', '01:02:03:04'),
        )
    )
    def test_parametrized(self, time_str, expected):
        assert add_missing_colons(time_str) == expected


class TestParseTime:
    @freezegun.freeze_time(datetime.datetime(2000, 1, 1, 0, 0, 0))
    @pytest.mark.parametrize(
        'time_str, expected',
        (
            ('12:34', datetime.time(0, 12, 34)),
            ('12:34:56', datetime.time(12, 34, 56)),
            ('12 34', datetime.time(0, 12, 34)),
            ('12Ж34', datetime.time(0, 12, 34)),
            ('12ж34', datetime.time(0, 12, 34)),
            ('12-34', datetime.time(0, 12, 34)),
        )
    )
    def test_parametrized(self, time_str, expected):
        result = parse_time(time_str)
        print(result)
        assert result == expected
