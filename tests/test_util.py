import pytest

from ffmpeg_interactive.util import add_missing_colons


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
