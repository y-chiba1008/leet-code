import pytest
from main import Solution

arg_names = ['s', 'numRows', 'expect']
arg_values = [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ('A', 1, 'A'),
    ('ABC', 1, 'ABC'),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_zigzag_conversion(s: str, numRows: int, expect: str):
    solution = Solution()
    result = solution.convert(s, numRows)
    assert result == expect
