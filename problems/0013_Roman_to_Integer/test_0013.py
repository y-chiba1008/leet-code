import pytest
from main import Solution

arg_names = ['s', 'expect']
arg_values = [
    ('III', 3),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_roman_to_int(s: str, expect: int):
    solution = Solution()
    result = solution.romanToInt(s)
    assert result == expect
