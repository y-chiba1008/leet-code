import pytest
from .main import Solution

arg_names = ['x', 'expect']
arg_values = [
    (121, True),
    (-121, False),
    (10, False),
]


@pytest.mark.parametrize(
    argnames=arg_names,
    argvalues=arg_values,
    ids=[f'case_{i}' for i in range(len(arg_values))],
)
def test_normal(x: int, expect: bool):
    solution = Solution()
    result = solution.isPalindrome(x)
    assert result == expect
