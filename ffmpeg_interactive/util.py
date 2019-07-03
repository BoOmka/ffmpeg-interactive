def add_missing_colons(time_str: str) -> str:
    colons = time_str.count(':')
    return f'{"00:" * (2 - colons)}{time_str}'
